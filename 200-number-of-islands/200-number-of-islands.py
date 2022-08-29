class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        xgrid = [[-1 for _ in range(m+2)] for _ in range(n+2)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    xgrid[i+1][j+1] = 0
                    
        def sub(i, j, cnt):
            if xgrid[i][j] == 0:
                xgrid[i][j] = cnt
            
                sub(i-1, j, cnt)
                sub(i+1, j, cnt)
                sub(i, j-1, cnt)
                sub(i, j+1, cnt)

            
        cnt = 0
        for i in range(n+2):
            for j in range(m+2):
                if xgrid[i][j] == 0:
                    cnt += 1
                    sub(i, j, cnt)
                    
        return cnt