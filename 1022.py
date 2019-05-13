# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def help(self, val, root: TreeNode):
        cur = ((val) << 1) + root.val
        if (not root.left and not root.right):
            return cur
        summ = 0
        if root.left:
            summ = self.help(cur, root.left)
        if root.right:
            summ = summ + self.help(cur, root.right)
        return summ
    def sumRootToLeaf(self,  root: TreeNode) ->int:
        return self.help(0, root)

