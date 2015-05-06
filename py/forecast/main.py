__author__ = 'yuanjie'


from datetime import date
import pandas as pd
import matplotlib.pyplot as plt


start_date = date(2014, 5, 1)
end_date = date(2014, 5, 12)

# Read data from csv files
df1 = pd.read_csv('data/series_xc_1.csv', index_col=0, header=0, parse_dates=0)
df2 = pd.read_csv('data/series_xc_2.csv', index_col=0, header=0, parse_dates=0)

# Generate date range from start to end
drange = pd.date_range(start_date, end_date, freq='1H', closed='left')

# Slice the sample data from start to end
df1 = df1.reindex(drange, method='bfill')
df1.columns = ['value1']
print "==========Series 1=========="
print df1.head()

df2 = df2.reindex(drange, method='bfill')
df2.columns = ['value2']
print "==========Series 2=========="
print df2.head()

# Combine df1 and df2
df = df1.join(df2)

# Calculate the sum of the every column
df = df.assign(
    total=lambda t: t.value1 + t.value2
)
df.drop(df.columns[[0, 1]], axis=1, inplace=True)
df.index.names = ['date']
print "==========Series=========="
print df.head()

# Load weather date
wh = pd.read_csv('data/weather_suzhou.csv', index_col=0, header=0, parse_dates=0)

# Slice the weather data from start to end
wh = wh.reindex(drange, method='bfill')
print "==========Weather Data=========="
print wh.head()

# Combine df and wh
df = df.join(wh[['TemperatureF', 'Humidity']])
print "==========Sample Data=========="
print df.head()

# Normalize
for col_name in df.columns:
    print 'Normalizing the column %s ...' % col_name
    col_min = df[col_name].min()
    col_max = df[col_name].max()
    df[col_name] = (df[col_name] - col_min) / (col_max - col_min)

# DEBUG: print plot
#df.plot()
#plt.show()


# ========================================================
#                 Create Neural Network
# ========================================================


from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection


# Create Forward Networks
net = FeedForwardNetwork()

# Create layer
in_layer = LinearLayer(2)
hidden_layer = SigmoidLayer(3)
out_layer = LinearLayer(1)

net.addInputModule(in_layer)
net.addModule(hidden_layer)
net.addOutputModule(out_layer)

# Create connection between layers
in_to_hidden = FullConnection(in_layer, hidden_layer)
hidden_to_out = FullConnection(hidden_layer, out_layer)

net.addConnection(in_to_hidden)
net.addConnection(hidden_to_out)

# Sort module
net.sortModules()


# ========================================================
#             Build the Datasets
# ========================================================

from pybrain.datasets import SupervisedDataSet

ds = SupervisedDataSet(2, 1)
for row in df.itertuples(index=False):
    print row[1:3]
    print row[0]
    ds.addSample(row[1:3], row[0])


# ========================================================
#             Training the network
# ========================================================

from pybrain.supervised.trainers import BackpropTrainer

trainer = BackpropTrainer(net, ds)
error = trainer.train()
while error >= 0.005:
    error = trainer.train()
    print 'Error=%f' % error


# ========================================================
#             Test the network
# ========================================================