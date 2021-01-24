'''
Algorithms Tags: DFS
Effeciency: Good

a simple dfs
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    balance = True

    def dfs(self, root):
        if not self.balance:
            return -1
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left-right) > 1:
            self.balance = False
        return max(left, right)+1

    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.balance
