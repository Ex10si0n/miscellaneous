'''
Algorithms Tags: None
Effeciency: Normal 50/82

Python OOP
'''
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.st = []
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.size += 1
            self.st.append(x)

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        ret = self.st.pop(self.size)
        return ret

    def increment(self, k: int, val: int) -> None:
        if k > self.size:
            k = self.size
        for i in range(k):
            self.st[i] += val
