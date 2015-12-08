from copy import deepcopy
from random import shuffle

def distinct(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def approx_equal(a, b, epsilon):
    return abs(a-b) <= epsilon

class Wire:
    """A Wire is a directed edge that can be used in a neural net to connect
    an input to a neuron, a neuron to a neuron, or a neuron to OUT."""
    def __init__(self, startNode, endNode, weight=1):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = weight

    def copy(self):
        return deepcopy(self)

    def __eq__(self, other, epsilon=0):
        try:
            return (self.startNode == other.startNode
                    and self.endNode == other.endNode
                    and approx_equal(self.weight, other.weight, epsilon))
        except:
            return False

    def __str__(self):
        return "Wire(%s, %s, %s)" % (str(self.startNode), str(self.endNode),
                                     str(self.weight))

    __repr__ = __str__  # this enables NeuralNet __str__ to print Wire objects

class NeuralNet:
    """A neural net is represented as a directed graph whose edges are Wires and
    nodes can be neurons, inputs, or OUT:
     - Each variable input is represented by its name (a string).
     - Each constant input is represented by an int or float (eg -1).
     - Each neuron is represented by its name (a string).
     - The final output is represented by the constant string NeuralNet.OUT."""

    OUT = 'OUT'

    def __init__(self, inputs=[], neurons=[], wires=[]):
        self.inputs = inputs[:]
        self.neurons = neurons[:]
        self.wires = wires[:]

    def get_wires(self, startNode=None, endNode=None):
        """Returns a list of all the wires in the graph.  If startNode or
        endNode are provided, restricts to wires that start/end at particular
        nodes.  (A node can be an input, a neuron, or the output OUT.)"""
        pred1 = lambda node: (startNode is None) or (node == startNode)
        pred2 = lambda node: (endNode is None)   or (node == endNode)
        return filter(lambda w: w is not None,
                      [w if pred1(w.startNode) and pred2(w.endNode)
                       else None for w in self.wires])

    def get_incoming_neighbors(self, node):
        """Returns an alphabetical list of neighboring nodes (neurons or inputs)
        that appear earlier in the neural net (that is, nodes that have wires
        leading into the provided node). Each node appears at most once."""
        return sorted(distinct(map(lambda w: w.startNode,
                                   self.get_wires(endNode=node))))

    def get_outgoing_neighbors(self, node):
        """Returns an alphabetical list of neighboring nodes (neurons or OUT)
        that appear later in the neural net (that is, nodes that receive the
        provided node's output). Each node appears at most once."""
        return sorted(distinct(map(lambda w: w.endNode,
                                   self.get_wires(startNode=node))))

    def get_incoming_wires(self, endNode):
        "Returns a list of wires leading into the provided neuron or OUT."
        return self.get_wires(endNode=endNode)

    def get_outgoing_wires(self, startNode):
        "Returns a list of wires exiting out of the provided neuron or input."
        return self.get_wires(startNode=startNode)

    def get_wire(self, startNode, endNode):
        """Returns the wire that directly connects startNode to endNode
        (or None if there is no such wire)"""
        wires = self.get_wires(startNode, endNode)
        return None if len(wires) == 0 else wires[0]

    def is_connected(self, startNode, endNode):
        """Returns True if there is a wire connecting startNode to endNode,
        otherwise False."""
        return any([endNode == w.endNode
                    for w in self.get_wires(startNode)])

    def has_incoming_neuron(self, node):
        """Returns True if node has at least one incoming neuron, otherwise
        False."""
        return any(map(lambda n: n in self.neurons,
                       self.get_incoming_neighbors(node)))

    def is_output_neuron(self, neuron):
        "Returns True if neuron is the output-layer neuron, otherwise False."
        return (neuron in self.neurons
                and bool(self.get_wire(neuron, NeuralNet.OUT)))

    def get_output_neuron(self):
        "Returns the name of the output-layer neuron."
        return self.get_incoming_neighbors(NeuralNet.OUT)[0]

    def topological_sort(self):
        """Returns a list of neurons sorted topologically, with input-layer
        neurons appearing first, and the output-layer neuron appearing last."""
        # Note: The reverse of a topologically sorted list is equivalent to the
        # topological sort of a reversed graph.  (This has been proved.)
        def append_earlier_nodes(topo_list, node):
            if node in topo_list:
                return topo_list
            for earlier_node in self.get_incoming_neighbors(node):
                if earlier_node in self.inputs:
                    continue
                topo_list = append_earlier_nodes(topo_list, earlier_node)
            return topo_list + [node]
        output_neuron = self.get_incoming_neighbors(NeuralNet.OUT)[0]
        return append_earlier_nodes([], output_neuron)

    def join(self, startNode, endNode, weight=1):
        "Adds a Wire between two nodes"
        if startNode not in self.neurons + self.inputs:
            print "NeuralNet.join: Adding", startNode, "to list of neurons"
            self.neurons.append(startNode)
        if endNode not in self.neurons + [NeuralNet.OUT]:
            print "NeuralNet.join: Adding", endNode, "to list of neurons"
            self.neurons.append(endNode)
        if self.is_connected(startNode, endNode):
            print "NeuralNet.join: Error adding wire: nodes already connected"
            return self
        self.wires.append(Wire(startNode, endNode, weight))
        return self

    def shuffle_lists(self):
        """Randomly reorders elements within each attribute list, resulting in
        an equivalent neural net."""
        map(shuffle, [self.inputs, self.neurons, self.wires])
        return self

    def copy(self):
        return deepcopy(self)

    def __eq__(self, other, epsilon=0):
        wire_key = lambda w: str(w.startNode) + '-' + str(w.endNode)
        sort_wires = lambda wires: sorted(wires, key=wire_key)
        try:
            assert sorted(self.inputs) == sorted(other.inputs)
            assert sorted(self.neurons) == sorted(other.neurons)
            assert len(self.wires) == len(other.wires)
            assert all([w1.__eq__(w2, epsilon) for w1, w2
                        in zip(*map(sort_wires, [self.wires, other.wires]))])
            return True
        except:
            return False

    def __str__(self):
        len_and_str = lambda x: tuple([fn(x) for fn in (len, str)])
        return ('NeuralNet with:'
                + '\n * %i inputs: %s' % len_and_str(self.inputs)
                + '\n * %i neurons: %s' % len_and_str(self.neurons)
                + '\n * %i wires: %s' % len_and_str(self.wires))

    __repr__ = __str__


# Rectified Linear Unit (an alternative to stairstep or sigmoid)
def ReLU(x):
    return max(x, 0)

__all__ = ['Wire', 'NeuralNet', 'ReLU', 'approx_equal']
