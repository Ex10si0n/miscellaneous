'''
Algorithms Tags: DFS
Effeciency: Normal

Find the same dfs-sequence
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, TreeNode, trace):
        if TreeNode is None:
            trace.append(None)
            return
        trace.append(TreeNode.val)
        self.dfs(TreeNode.left, trace)
        self.dfs(TreeNode.right, trace)


    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        trace_p = list()
        trace_q = list()
        self.dfs(p, trace_p)
        self.dfs(q, trace_q)
        if trace_p == trace_q:
            return True
        return False
