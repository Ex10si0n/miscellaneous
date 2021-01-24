'''
Algorithms Tags: None
Effeciency: Good

Simple linked-list implementation
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_int(l):
            return l.val + 10 * to_int(l.next) if l else 0
        def to_list(val):
            l = ListNode(val % 10)
            if val > 9:
                l.next = to_list(val // 10)
            return l
        return to_list(to_int(l1) + to_int(l2))
