__author__ = 'yuanjie'


from datetime import date
import pandas as pd
from pybrain.datasets import SupervisedDataSet
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

errors = nn.train_network(net, ds, 0.00001)
err_df = pd.DataFrame(errors)
err_df.columns = ['error']
# print err_df.head()

# DEBUG: Draw error plot
err_df.plot()
plt.show()

# ========================================================
#                  Test the network
# ========================================================

test_results = nn.validate_network(df, net, in_count)
test_df = pd.DataFrame(test_results)
test_df.columns = ['result', 'expect', 'error']

# DEBUG: Draw testing results plot
test_df.plot()
plt.show()

# ========================================================
#                  Validate network
# ========================================================

# Load cross validate sample date
cv = sampler.load_sample(date(2014, 5, 12), date(2014, 5, 18))

# Run cross validate
cv_results = nn.validate_network(cv, net, in_count)
cv_df = pd.DataFrame(test_results)
cv_df.columns = ['result', 'expect', 'error']

# DEBUG: Draw testing results plot
cv_df.plot()
plt.show()
