'''
Algorithms Tags: BFS
Effeciency: Good

A simple bfs, then get it
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = list()
        dep = list()
        q.append(root)
        dep.append(1)
        while q:
            x = q.pop(0)
            d = dep.pop(0)
            print(d)
            if x is None:
                return 0
            if x is not None and (x.left is None and x.right is None):
                return d
            if x.left:
                q.append(x.left)
                dep.append(d+1)
            if x.right:
                q.append(x.right)
                dep.append(d+1)
