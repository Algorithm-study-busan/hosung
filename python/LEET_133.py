"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self) :
        self.visited = dict()

    def dfs(self, node, copy) :
        for neighbor in node.neighbors :
            if neighbor in self.visited : 
                copy.neighbors.append(self.visited[neighbor])
            else :
                copy_neighbor = Node(neighbor.val, [])
                self.visited[neighbor] = copy_neighbor
                copy.neighbors.append(copy_neighbor)
                self.dfs(neighbor, copy_neighbor)
                
                
    

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None : return None
        copy = Node(node.val, [])
        self.visited[node] = copy
        self.dfs(node, copy)
        return copy
        