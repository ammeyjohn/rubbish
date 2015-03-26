__author__ = 'patrick'

import Sampler

from pybrain.structure import TanhLayer, SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

inputs, outputs = Sampler.load_csv('data/sample.csv', 3)

ds = SupervisedDataSet(3, 1)
for i in range(0, len(inputs)):
    ds.addSample(inputs[i], outputs[i])

net = buildNetwork(3, 6, 1, bias=True, hiddenclass=SigmoidLayer)

trainer = BackpropTrainer(net, ds)

error = 1.0
while error > 0.0001:
    error = trainer.train()
    print 'Error = %f' % error

res = net.activate([1, 0, 1])
print 'Result = %f' % res