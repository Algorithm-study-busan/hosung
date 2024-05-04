# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeTree(self, pre_l, pre_r, in_l, in_r, preorder, inorder) :
        if pre_l > pre_r : return None
        if pre_l == pre_r : return TreeNode(preorder[pre_l], None, None)
        root_val = preorder[pre_l]
        
        in_root_idx = -1
        for i in range(in_l, in_r+1) :
            if inorder[i] == root_val : in_root_idx = i
        
        left_pre_l = pre_l+1
        left_pre_r = pre_l + in_root_idx - in_l
        left_in_l = in_l
        left_in_r = in_root_idx - 1

        right_pre_l = pre_l + in_root_idx - in_l + 1
        right_pre_r = pre_r
        right_in_l = in_root_idx + 1
        right_in_r = in_r
        
        return TreeNode(root_val, self.makeTree(left_pre_l, left_pre_r, left_in_l, left_in_r, preorder, inorder), self.makeTree(right_pre_l, right_pre_r, right_in_l, right_in_r, preorder, inorder))

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lenght = len(preorder)
        return self.makeTree(0, lenght-1, 0, lenght-1, preorder, inorder) 
        