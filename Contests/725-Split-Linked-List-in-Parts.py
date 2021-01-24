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

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans = []
        _len = 0
        each = root
        while each:
            _len += 1
            each = each.next
        base = _len // k
        upper = _len % k
        for i in range(k):
            if upper > 0:
                strip = base + 1
            else:
                strip = base
            upper -= 1
            head = ListNode(0)
            copy = head
            for j in range(strip):
                if root is not None:
                    copy.next = ListNode(root.val)
                    copy = copy.next
                    root = root.next
                else:
                    head.next = None
                    break
            ans.append(head.next)
        return ans
