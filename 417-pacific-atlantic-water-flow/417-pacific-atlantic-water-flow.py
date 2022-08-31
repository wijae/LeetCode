class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        
        flood = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
        
        def flood_sub(i, j, color):
            if not flood[i][j][color]:
                flood[i][j][color] = True
                
                if i>0 and heights[i][j] <= heights[i-1][j]:
                    flood_sub(i-1, j, color)
                
                if j>0 and heights[i][j] <= heights[i][j-1]:
                    flood_sub(i, j-1, color)
                
                if i+1<n and heights[i][j] <= heights[i+1][j]:
                    flood_sub(i+1, j, color)
                
                if j+1<m and heights[i][j] <= heights[i][j+1]:
                    flood_sub(i, j+1, color)
                    
        for i in range(n):
            flood_sub(i, 0, 0)
            flood_sub(i, m-1, 1)
            
        for j in range(m):
            flood_sub(0, j, 0)
            flood_sub(n-1, j, 1)
            
        ans = []
        for i in range(n):
            for j in range(m):
                if flood[i][j][0] and flood[i][j][1]:
                    ans.append([i, j])
                    
        return ans