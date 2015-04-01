__author__ = 'yuanjie'

from pybrain.structure import RecurrentNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets.sequential import SequentialDataSet
import sampler
import pandas as pd

# Defines the parameters
windowSize = 10

# Defines the neural count for each layer
inLayerCount = 2
hiddenLayerCount = 3
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

# Create bp trainer
# trainer = BackpropTrainer(net, None)

# Load sample data as Series
ts = sampler.load_csv('data/series.csv')
print(ts.head(10))

# Get the min and max value in series
vmin = ts.min(axis=0)
vmax = ts.max(axis=0)
print 'min = %f, max = %f' % (vmin, vmax)

# Normalize
ts = (ts - vmin) / (vmax - vmin)
print(ts.head(10))

# Create window size dataset
mtx = {}
for i in range(0, windowSize):
    mtx[i] = ts.shift(i)

df = pd.DataFrame(mtx)
print df.head(20)

# Create datasets
ds = SequentialDataSet(2, 1)

for row in range(windowSize, 100):
    for col in range(windowSize, 0, -1):
        pass