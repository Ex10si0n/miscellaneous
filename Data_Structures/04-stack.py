from 01-node import *

class stack(object):

    def __init__(self):
        '''[attr] t: top, l: length'''
        self.t = None
        self.l = 0

    def __bool__(self):
        return self.t is not None

    def push(self, x):
        self.t = Node(x, self.t)
        self.l += 1
    
    def top(self):
        if not self:
            raise IndexError
        return self.t.v

    def pop(self):
        x = self.top()
        self.t = self.t.n
        self.l -= 1
        return x

    def __iter__(self):
        p = self.t
        while p:
            yield p.v
            p = p.n
    
    def __repr__(self):
        rep = '[Linked List] '
        if self.t is None:
            return rep + 'Empty'
        for i, y in enumerate(self):
            rep += str(y) + ' → '
        rep = rep[:-2]
        return rep

    def __len__(self):
        return self.l
