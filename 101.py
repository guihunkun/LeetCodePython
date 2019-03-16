# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.help(root.left,root.right)
    def help(self, left: TreeNode,right: TreeNode) -> bool:
        if not left and not right:
            return True;
        if not left or not right:
            return False
        if left.val!=right.val:
            return False
        return (self.help(left.left,right.right) and self.help(left.right,right.left))
