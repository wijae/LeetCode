class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ml, mr = [0 for _ in range(n)], [0 for _ in range(n)]
        
        ml[0] = height[0]
        for i in range(1, n):
            ml[i] = max(ml[i-1], height[i])
        
        mr[n-1] = height[n-1] 
        for i in range(n-2, -1, -1):
            mr[i] = max(mr[i+1], height[i])
            
        ans = 0
        for i in range(n):
            ans += max(0, min(ml[i], mr[i]) - height[i])
            
        return ans