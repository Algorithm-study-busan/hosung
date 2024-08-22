# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if root is None : return None

        left_node = self.flatten(root.left)
        right_node = self.flatten(root.right)

        root.left = None
        if left_node is None :
            root.right = right_node
        else :
            tmp = left_node
            while tmp.right :
                tmp = tmp.right
            tmp.right = right_node
            root.right = left_node

        return root
        