'''
Algorithms Tags: DFS
Effeciency: Normal 70

dfs two times
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs0(self, treenode, trace):
        if treenode == None:
            trace.append(None)
            return
        trace.append(treenode.val)
        self.dfs0(treenode.left, trace)
        self.dfs0(treenode.right, trace)


    def dfs1(self, treenode, trace):
        if treenode == None:
            trace.append(None)
            return
        trace.append(treenode.val)
        self.dfs1(treenode.right, trace)
        self.dfs1(treenode.left, trace)


    def isSymmetric(self, root: TreeNode) -> bool:
        lr = list()
        rl = list()
        self.dfs0(root, lr)
        self.dfs1(root, rl)
        # print(lr, rl)
        if lr == rl:
            return True
        return False
