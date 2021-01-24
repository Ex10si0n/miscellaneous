'''
Algorithms Tags: None
Effeciency: Good 98

Simple linked-list implementation
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        start = head
        _len = 0
        while head:
            _len += 1
            head = head.next
        if k == 0 or _len == 0 or _len == 1 or k % _len == 0:
            return start
        k %= _len
        head = start
        _len = _len - k - 1
        while _len:
            _len -= 1
            head = head.next
        end = head.next
        new_start = end
        head.next = None
        while end.next:
            end = end.next
        end.next = start
        return new_start
