# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def sub(node):
            if node is None:
                return False
            
            sl, sr = sub(node.left), sub(node.right)
            if not sl:
                node.left = None
            
            if not sr:
                node.right = None
                
            if node.val == 1:
                return True
            
            return sl or sr
        
        if not sub(root):
            return None
        else:
            return root
            
                
        