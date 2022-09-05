"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        
        def sub(node, depth):
            if node is None:
                return
            
            if len(ans) <= depth:
                ans.append([])
                
            ans[depth].append(node.val)
            
            for child in node.children:
                sub(child, depth + 1)
                
        sub(root, 0)
        return ans