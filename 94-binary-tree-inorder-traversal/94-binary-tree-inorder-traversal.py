# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def sub(node):
            return ([] if node.left is None else sub(node.left)) + [node.val] + ([] if node.right is None else sub(node.right))
        
        return [] if root is None else sub(root)
            
            