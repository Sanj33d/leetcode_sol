"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # creting floating nodes
        old_to_new = {} # storing the address of floating nodes corresponding the old ones
        visited = set() # to prevent multiple visits
        stk = [] # to loop the creation of new_nodes
        start = node

        visited.add(start)
        stk.append(start)

        while stk:
            cur = stk.pop()
            old_to_new[cur] = Node(cur.val)

            for nei in cur.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)

        # connecting the floating nodes
        for old_node, new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_nei = old_to_new[nei]
                new_node.neighbors.append(new_nei) 
        
        return old_to_new[start]
