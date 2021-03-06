__author__ = 'patrick'


from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet


def create_ff_network(options):
    """Create the FeedForware network
    :param options: The input options.
    :return:
    """

    # Create FF network
    net = FeedForwardNetwork()

    # Create each Layer instance
    in_layer = LinearLayer(options['inUnitCount'])
    hidden_layer = SigmoidLayer(options['hiddenUnitCount'])
    out_layer = LinearLayer(options['outUnitCount'])

    # Build network layer topology
    net.addInputModule(in_layer)
    net.addModule(hidden_layer)
    net.addOutputModule(out_layer)

    in_to_hidden = FullConnection(in_layer, hidden_layer)
    hidden_to_out = FullConnection(hidden_layer, out_layer)

    net.addConnection(in_to_hidden)
    net.addConnection(hidden_to_out)

    # Complete structure network
    net.sortModules()

    return net


def train_network(net, ds, diff_error):
    errors = []
    trainer = BackpropTrainer(net, ds)
    error = trainer.train()
    errors.append(error)
    diff = 10000
    while diff >= diff_error:
        error1 = trainer.train()
        errors.append(error1)
        diff, error = abs(error1 - error), error1
        print 'Error=%f, Diff=%f' % (error1, diff)

    return errors


def validate_network(df, net, in_count):
    results = []
    sigma = 0
    for row in df.itertuples(index=False):
        result = net.activate(row[1:in_count+1])[0]
        expect = row[0]
        error = (expect - result) ** 2
        results.append([result, expect, error])
        sigma += error
        print 'Result = %f, Expect = %f, Test Error = %f' % (result, expect, error)

    print 'Sigma of testing error = %f' % sigma

    return results