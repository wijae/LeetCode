# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, arr):
            ans = 0
            arr[node.val] += 1
                
            if node.left:
                ans += dfs(node.left, list(arr))
            
            if node.right:
                ans += dfs(node.right, list(arr))
                
            if node.left is None and node.right is None:
                cnt = 0
                for i in range(10):
                    if (arr[i] % 2) == 1:
                        cnt += 1

                if cnt <= 1:
                    ans += 1
                
            return ans
                
                
        return dfs(root, [0 for _ in range(10)])