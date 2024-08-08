# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None : return False

        ans = [False]
        def dfs(root, tmp, ans) :
            if root.left is None and root.right is None :
                if tmp + root.val == targetSum : 
                    ans[0]  = True
                return
            if root.left is not None :
                dfs(root.left, tmp+root.val, ans)
            if root.right is not None :
                dfs(root.right, tmp+root.val, ans)
        dfs(root, 0, ans)
        return ans[0]
        