# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_node_count = []
        level_node_sum = []
        
        def dfs(node, level):
            if node is None:
                return
            
            if len(level_node_count) <= level:
                level_node_count.append(0)
        
            if len(level_node_sum) <= level:
                level_node_sum.append(0)
                
            level_node_count[level] += 1
            level_node_sum[level] += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        
        ans = []
        for i in range(len(level_node_count)):
            ans.append(level_node_sum[i]/level_node_count[i])
            
        return ans