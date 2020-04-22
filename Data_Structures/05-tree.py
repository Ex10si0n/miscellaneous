from 01-node import *

class btree(object):

    def __init__(self, root):
        '''[attr] r: root, l: left_child, r: right_child'''
        self.v = root
        self.l = None
        self.r = None
        self.s = 1

    def insl(self, new_node):
        self.s += 1
        if self.l is None:
            self.l = btree(new_node)
        else:
            t = btree(new_node)
            t.l = self.l
            self.l = t
    
    def insr(self, new_node):
        self.s -= 1
        if self.r is None:
            self.r = btree(new_node)
        else:
            t = btree(new_node)
            t.r = self.r
            self.r = t

    def dell(self):
        if self.l is None:
            raise IndexError
        else:
            self.l = None
            self.s -= 1

    def delr(self):
        if self.r is None:
            raise IndexError
        else:
            self.r = None
            self.s -= 1

    def setv(self, value):
        self.v = value

    def getv(self):
        return self.v
    
    def bfs(self, root):
        rep = []
        q = []
        q.append(root)
        while q:
            now = q.pop(0)
            rep.append(now.v)
            if now.l:
                q.append(now.l)
            else:
                rep.append('null')
            if now.r:
                q.append(now.r)
            else:
                rep.append('null')
        return str(rep)

    def tr(self):
        rep = self.bfs(self)
        
    def __repr__(self):
        rep = '[btree] ' + self.bfs(self)
        return str(rep)
