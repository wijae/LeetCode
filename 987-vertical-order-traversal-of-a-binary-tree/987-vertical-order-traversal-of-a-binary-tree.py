# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos = {}
        
        def sub(node, x, y):
            if node is None:
                return
            
            if y not in pos:
                pos[y] = {}
                
            if x not in pos[y]:
                pos[y][x] = []
                
            pos[y][x].append(node.val)
            
            sub(node.left, x+1, y-1)
            sub(node.right, x+1, y+1)
            
        
        sub(root, 0, 0)
        
        ans = []
        for y in sorted(pos.keys()):
            ans_sub = []
            for x in sorted(pos[y].keys()):
                ans_sub += sorted(pos[y][x])
                
            ans.append(ans_sub)
        
        return ans