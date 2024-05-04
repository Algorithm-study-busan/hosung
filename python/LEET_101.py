# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, l, r) : 
        if l is None and r is None : return True
        if l is None or r is None : return False

        if l.val != r.val : return False
        return self.solve(l.left, r.right) and self.solve(l.right, r.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root.left, root.right)
        