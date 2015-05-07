__author__ = 'yuanjie'


from datetime import date
import pandas as pd
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import matplotlib.pyplot as plt
import sampler
import nn

in_count = 4
hidden_count = 5
out_count = 1

# ========================================================
#                  Load Sample Data
# ========================================================

start_date = date(2014, 5, 5)
end_date = date(2014, 5, 11)
df = sampler.load_sample(start_date, end_date)

# ========================================================
#                  Create FF Network
# ========================================================

option = {
    'inUnitCount': in_count,
    'hiddenUnitCount': hidden_count,
    'outUnitCount': out_count
}
net = nn.create_ff_network(option)

# ========================================================
#                 Build the Datasets
# ========================================================

ds = SupervisedDataSet(in_count, out_count)
for row in df.itertuples(index=False):
    ds.addSample(row[0:in_count], row[in_count])

# ========================================================
#                 Training the network
# ========================================================

trainer = BackpropTrainer(net, ds)
error = trainer.train()
diff = 10000
while diff >= 0.000001:
    error1 = trainer.train()
    diff, error = abs(error1 - error), error1
    print 'Error=%f, Diff=%f' % (error1, diff)


# ========================================================
#                  Test the network
# ========================================================

test_sigma = 0
for row in df.itertuples(index=False):
    result = net.activate(row[0:in_count])
    expect = row[in_count]
    error = (expect - result) ** 2
    test_sigma += error
    print 'Result = %f, Expect = %f, Test Error = %f' % (result, expect, error)

print 'Sigma of testing error = %f' % test_sigma

# ========================================================
#                  Validate network
# ========================================================

# Load cross validate sample date
cv = sampler.load_sample(date(2014, 5, 12), date(2014, 5, 18))

cv_sigma = 0
for row in cv.itertuples(index=False):
    result = net.activate(row[0:in_count])
    expect = row[in_count]
    error = (expect - result) ** 2
    cv_sigma += error
    print 'Result = %f, Expect = %f, CV Error = %f' % (result, expect, error)

print 'Sigma of cv error = %f' % test_sigma
