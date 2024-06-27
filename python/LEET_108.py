# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeTree(self, nums, lo, hi) :
        if lo > hi : return
        mid = (lo + hi)//2
        
        tree = TreeNode(nums[mid])
        tree.left = self.makeTree(nums, lo, mid-1) 
        tree.right = self.makeTree(nums, mid+1, hi)
        return tree

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeTree(nums, 0, len(nums)-1)
        
        