class Node(object):

    def __init__(self, value, next_node):
        '''[attr] v: value, n: next'''
        self.v = value
        self.n = next_node
        self.ev = []

class DoubleNode(Node):

    def __init__(self, value, successor, precursor):
        '''[attr] v: value, n: successors, p: precursor'''
        self.v = value
        self.n = successor
        self.p = precursor
