# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(root, arr, ans) :
            if root is None : return
            arr.append(root.val) 
            if root.left is None and root.right is None :
                for i in range(len(arr)) :
                    ans[0] += arr[-(i+1)] * 10**i
                arr.pop()
                return
            dfs(root.left, arr, ans)
            dfs(root.right, arr, ans)
            arr.pop()
        dfs(root, [], ans)
        return ans[0]
                
        