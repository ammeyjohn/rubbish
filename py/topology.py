class Graph:
    def __init__(self):
        self.__nodes = {}
        self.__edges = {}

    def add_node(self, name, value):
	node = self.__nodes.get(name) 
	if node == None:
            node = Node(name, value)
            node.__graph = self
            self.__nodes[name] = node
	return node

class Node:
    def __init__(self, name, value):        
        self.name = name
        self.value = value
        self.__graph = None
        self.__edges = []

    def connect(self, edge):
        self.__edges.append(edge)

    def __repr__(self):        
        return "Name=%s, Value=%s" % (self.name, self.value)

class Edge:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.__graph = None
        self.__node0 = None
        self.__node1 = None

    def connect(self, node0, node1):
        self.__node0 = node0
        self.__node1 = node1

    def __repr__(self):
        return "From: %s, To: %s" % (self.__node0, self.__node1)

def test():
	g = Graph()
	n0 = g.add_node("Node0", 1)
	n1 = g.add_node("Node1", 2)
