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

    if options is None:
        options = {
            'inUnitCount': 2,
            'hiddenUnitCount': 3,
            'outUnitCount': 1
        }

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



