'''
Algorithms Tags: DFS
Effeciency: Normal

A Simple dfs trace for a bin-tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_dep = 0

    def dfs(self, treenode, depth):
        if treenode is None:
            self.max_dep = max(depth, self.max_dep)
            return
        self.dfs(treenode.left, depth+1)
        self.dfs(treenode.right, depth+1)


    def maxDepth(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.max_dep
