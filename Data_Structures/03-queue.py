from 01-node import *

class queue(object):

    def __init__(self):
        '''[attr] h: head, t: tail, l: length'''
        self.h = None
        self.t = self.h
        self.l = 0
    
    def __bool__(self):
        return self.t is not None

    def head(self):
        if not self:
            raise IndexError
        return self.h.v
    
    def tail(self):
        if not self:
            raise IndexError
        return self.t.v

    def push_back(self, x):
        if self.l == 0:
            self.h = self.t = DoubleNode(x, self.t, None)
            self.l += 1
        else:
            self.t = DoubleNode(x, self.t, None)
            self.t.n.p = self.t
            self.l += 1

    def pop(self):
        x = self.head()
        self.h.p.n = None
        self.h = self.h.p
        self.l -= 1
        return x

    def __iter__(self):
        p = self.h
        while p:
            yield p.v
            p = p.p
    
    def __repr__(self):
        rep = '[Queue] '
        p = self.t
        while p is not None:
            rep += str(p.v) + ' → '
            p = p.n
        rep = rep[:-2]
        return rep

    def __len__(self):
        return self.l
