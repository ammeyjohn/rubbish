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
import weather

# Defines the parameters
columns = 3
windowSize = 2
delta_error = 0.0005

# Defines the neural count for each layer
inLayerCount = 3
outLayerCount = 1
hiddenLayerCount = 6

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

# Load sample data as DataFrame
print 'Loading sample data from csv file ...'
df = sampler.load_csv_frame('data/series30.csv')
print df.head()


# Normalize
for col_name in df.columns:
    print 'Normalizing the column %s ...' % col_name
    col_min = df[col_name].min()
    col_max = df[col_name].max()
    df[col_name] = (df[col_name] - col_min) / (col_max - col_min)

print df.head()
# df.plot()
# plt.show()

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
    ds.addSample(row[0:columns-2], row[columns-2])

ds.endOfData()

# Create bp trainer
trainer = BackpropTrainer(net, ds)

# Trains the datasets
print 'Training ...'
epoch = 5000
error = 1.0
while error > delta_error and epoch >= 0:
    error = trainer.train()
    epoch -= 1
    print 'Epoch = %d, Error = %f' % (epoch, error)

sum_err = 0
for row in df.itertuples(index=False):
    result = net.activate(row[0:columns-2])
    expect = row[columns-2]
    error = abs(expect - result)
    sum_err = sum_err + error
    print 'Result = %f, Expect = %f, Error = %f' % (result, expect, error)

print 'Total Error = %f' % sum_err