# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def sub(node):
            if node.left is None and node.right is None:
                return str(node.val)
            
            ans = str(node.val)
            if node.left is not None:
                ans += "(" + sub(node.left) + ")"
            else:
                ans += "()"
                
            if node.right is not None:
                ans += "(" + sub(node.right) + ")"
                
            return ans
            
        return sub(root)