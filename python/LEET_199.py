# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) :
        self.ans = [0 for _ in range(1000)]
        self.max_depth = -1

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root, 0)
        return self.ans[:self.max_depth+1]
        

    def dfs(self, root, depth) :
        if root is None : return

        self.max_depth = max(self.max_depth, depth)
        self.ans[depth] = root.val

        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)


        