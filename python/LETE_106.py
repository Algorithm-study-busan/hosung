# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def bs(inorder, postorder, in_l, in_r, post_l, post_r) :
            if in_l > in_r : return None
            node = TreeNode(postorder[post_r])

            root_idx = -1
            for i in range(in_l, in_r+1) :
                if inorder[i] == node.val : 
                    root_idx = i
                    break 

            nxt_left_in_l = in_l
            nxt_left_in_r = root_idx-1
            nxt_left_post_l = post_l 
            nxt_left_post_r = post_l + root_idx-in_l-1

            nxt_right_in_l = root_idx+1
            nxt_right_in_r = in_r
            nxt_right_post_l = post_l + root_idx-in_l
            nxt_right_post_r = post_r-1

            node.left = bs(inorder, postorder, nxt_left_in_l, nxt_left_in_r, nxt_left_post_l, nxt_left_post_r)
            node.right = bs(inorder, postorder, nxt_right_in_l, nxt_right_in_r, nxt_right_post_l, nxt_right_post_r)

            return node

        N = len(inorder)-1
        return bs(inorder, postorder, 0,N,0,N)
        

            

        