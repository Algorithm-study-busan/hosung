# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-987654321]
        def dfs(root, ans) :
            if root is None : return 0
            left = max(dfs(root.left, ans), 0)
            right = max(dfs(root.right, ans), 0)
            ans[0] = max(ans[0], root.val + left + right)
            
            return root.val + max(left, right)

        dfs(root, ans)
        return ans[0]
            
        