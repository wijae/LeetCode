# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            ans = 0
            if max_val <= node.val:
                ans += 1
                
            if node.left:
                ans += dfs(node.left, max(max_val, node.val))
            
            if node.right:
                ans += dfs(node.right, max(max_val, node.val))
            
            return ans
        
        return dfs(root, root.val)