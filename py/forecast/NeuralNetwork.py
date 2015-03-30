__author__ = 'patrick'

import pandas as pd

from pybrain.structure import TanhLayer, SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

# Load data from csv file
series = pd.read_csv('data/series.csv')

# Add data to DataSet
ds = SupervisedDataSet(2, 1)
# for i in range(0, len(inputs)):
#     ds.addSample(inputs[i], outputs[i])

# Create neural network and trainer
net = buildNetwork(2, 3, 1)
trainer = BackpropTrainer(net, ds, batchlearning=True)

# Iterate to train
error = 1.0
while error > 0.0005:
    error = trainer.train()
    print 'Error = %f' % error

# Forecast by the given inputs
res = net.activate([0, 0.269417, 0.275875, 0.257267, 0.263624, 0.265362])
print 'Result = %f' % res

val = res * (6232.655 - 2347.186) + 2347.186
print 'Value = %f' % val

err_rate = (val-3284.571)/3284.571*100
print 'Error Rate = %f' % err_rate