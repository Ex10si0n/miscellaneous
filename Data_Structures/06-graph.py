from 01-node import *

class graph(object):

    def __init__(self):
        '''[attr] s: node_num, e: edge_num'''
        self.s = 0
        self.e = 0
        self.node = []
        
    def get(self, value):
        for node in self.node:
            if node.v == value:
                return node
                break
        raise IndexError

    def inse(self, from_node, to_node, value):
        f = self.get(from_node)
        t = self.get(to_node)
        if self.s < 2:
            raise IndexError
        if t not in f.n:
            f.n.append(t)
            f.ev.append(value)
            self.e += 1  
        else:
            for i in range(len(f.n)):
                if f.n[i] == t:
                    f.ev[i] = value
                    break

    def insn(self, node):
        self.s += 1
        self.node.append(Node(node, []))

if __name__ == "__main__":
    g = graph()
    g.insn('c')
    g.insn('b')
    g.insn('d')
    g.insn('f')
    g.insn('e')
    g.insn('a')
    g.inse('c', 'b', 1)
    g.inse('b', 'a', 1)
    g.inse('a', 'e', 1)
    g.inse('e', 'f', 1)
    g.inse('f', 'd', 1)
    g.inse('d', 'b', 1)

    c = g.get('c')
    for i in range(20):
        print(c.v)
        c = c.n[0]
        