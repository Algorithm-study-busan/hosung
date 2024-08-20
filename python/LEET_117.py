"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        arr = [0 for _ in range(6001)]

        def dfs(node, depth) :
            if node is None : return
            if arr[depth] == 0 :
                arr[depth] = node
            else :
                arr[depth].next = node
                arr[depth] = node
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)        

        return root