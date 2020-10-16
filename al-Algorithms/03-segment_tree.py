#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SegmentTree:
	def __init__(self, arr):
		self.arrLen = len(arr)
		self.seg = [0 for i in range(2 * self.arrLen)]
		for i in range(self.arrLen, 2*self.arrLen):
			self.seg[i] = [arr[i-self.arrLen]]
		for i in range(self.arrLen-1, 0, -1):
			self.seg[i] = self.seg[2*i] + self.seg[2*i+1]

	def update(self, i, value):
		i = i + self.arrLen
		self.seg[i] = [value]
		while i > 1:
			i //= 2
			self.seg[i] = self.seg[2*i] + self.seg[2*i+1]

	def __str__(self):
		retr = ''
		exp = 1
		cnt = 1
		for i in range(1, len(self.seg)):
			cnt -= 1
			retr += str(self.seg[i])
			if cnt == 0:
				exp *= 2
				cnt = exp
				retr += '\n'
		return retr
# 有bug


if __name__ == '__main__':
	segt = SegmentTree([0, 1, 2, 3, 4, 5, 6, 7])
	print(segt)
	segt.update(4, "Hello")
	print(segt)

