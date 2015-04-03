__author__ = 'yuanjie'

import math
from pybrain.structure import RecurrentNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets.sequential import SequentialDataSet, SupervisedDataSet
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sampler

# Defines the parameters
windowSize = 2
delta_error = 0.1

# Defines the neural count for each layer
inLayerCount = 2
outLayerCount = 1
hiddenLayerCount = 3

# Create recurrent network
print 'Creating recurrent network ...'
net = RecurrentNetwork()

# Add neural module
net.addInputModule(LinearLayer(inLayerCount, name='in'))
net.addModule(SigmoidLayer(hiddenLayerCount, name='hidden'))
net.addOutputModule(LinearLayer(outLayerCount, name='out'))

# Add neural connection
net.addConnection(FullConnection(net['in'], net['hidden'], name='in_to_hidden'))
net.addConnection(FullConnection(net['hidden'], net['out'], name='hidden_to_out'))

# Add recurrent connection
net.addRecurrentConnection(FullConnection(net['hidden'], net['hidden'], name='recurrent'))
net.sortModules()

# Load sample data as Series
print 'Loading sample data from csv file ...'
df = sampler.load_csv_frame('data/series.csv')
print df.head()

# Normalize
for col_name in df.columns:
    print 'Normalizing the column %s ...' % col_name
    col_min = df[col_name].min()
    col_max = df[col_name].max()
    df[col_name] = (df[col_name] - col_min) / (col_max - col_min)

print df.head()
df.plot()
plt.show()

# i1 = np.sin(np.arange(0, 20))
# i2 = np.sin(np.arange(0, 20)) * 2
#
# t1 = np.ones([1, 20])
# t2 = np.ones([1, 20]) * 2
#
# input = np.array([i1, i2, i1, i2]).reshape(20 * 4, 1)
# target = np.array([t1, t2, t1, t2]).reshape(20 * 4, 1)

# Create datasets
print 'Preparing dataset ...'
# ts = sampler.load_csv('data/series.csv')
ds = SequentialDataSet(inLayerCount, outLayerCount)
ds.newSequence()
# ds = SupervisedDataSet(inLayerCount, outLayerCount)

for row in df.itertuples(index=False):
    print row
    print row[0:2]
    print row[2]
    ds.addSample(row[0:2], row[2])

ds.endOfData()

# Create bp trainer
trainer = BackpropTrainer(net, ds)

# Trains the datasets
print 'Training ...'
error = 1.0
while error > delta_error:
    error = trainer.train()
    print 'Error = %f' % error

res = net.activate([0.63, 0.6])
print 'Result = %f, Expect = %f' % (res, 0.137)
