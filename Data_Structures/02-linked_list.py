class Node:
    def __init__(self, elm, nxt):
        self.elm = elm
        self.nxt = nxt


def reverse(h, p):
    if h is None:
        return p
    else:
        return reverse(h.nxt, Node(h.elm, p))


def print_n(node):
    while node:
        print(node.elm)
        node = node.nxt



def insert(h, i, x):
    if i < 0:
        raise IndexError
    if i == 0:
        return Node(x, h)
    if i == 1:
        h.nxt = Node(x, h.nxt)
    if h.nxt is not None:
        insert(h.nxt, i-1, x)
        return h
    else:
        raise IndexError

def remove(h, i):
    if i < 0:
        raise IndexError
    if i == 0:
        while h.nxt.nxt is not None:
            h.elm = h.nxt.elm
            h = h.nxt
        h.elm = h.nxt.elm
        h.nxt = None
        return
    while h.nxt is not None:
        i -= 1
        if i == 0:
            h.nxt = h.nxt.nxt
            return
        h = h.nxt
    raise IndexError

def rr_in(h, i, x):
    if i == 1:
        h.nxt = Node(x, h.nxt)
        return h
    elif i > 1:
        if h.nxt is None:
            raise IndexError
        else:
            return rr_in(h.nxt, i-1, x)
    else:
        raise IndexError

def main():
    h = Node(1, None)
    i = Node(2, h)
    j = Node(3, i)
    k = Node(4, j)
    print_n(k)
    remove(k, 0)
    print_n(k)


if __name__ == '__main__':
    main()
