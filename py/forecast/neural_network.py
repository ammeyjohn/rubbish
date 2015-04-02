__author__ = 'yuanjie'

from pybrain.structure import RecurrentNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets.sequential import SequentialDataSet, SupervisedDataSet
import sampler
import pandas as pd

# Defines the parameters
windowSize = 5
delta_error = 0.0005

# Defines the neural count for each layer
inLayerCount = windowSize + 1
hiddenLayerCount = inLayerCount * 2
outLayerCount = 1

# Create recurrent network
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
df = sampler.load_csv('data/sample.csv')

# Create datasets
# ds = SequentialDataSet(inLayerCount, outLayerCount)
# ds.newSequence()
ds = SupervisedDataSet(inLayerCount, outLayerCount)

idx = df.index.tolist()
print(len(idx))

for row in range(0, len(idx)):

    _in = [idx[row]]
    _out = [df.iloc[row, 0]]

    for col in range(1, 6):
        _in.append(df.iloc[row, col])

    ds.addSample(_in, _out)

# ds.endOfData()

# Create bp trainer
trainer = BackpropTrainer(net, ds)

# Trains the datasets
error = 1.0
while error > delta_error:
    error = trainer.train()
    print 'Error = %f' % error

res = net.activate(_in)
print 'Result = %f, Expect = %f' % (res, _out[0])
