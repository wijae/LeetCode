class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat[0]), len(mat)
        
        for d in range(-m, n):
            start = (d, 0) if d > 0 else (0, -d)
            
            arr = []
            for i in range(m+n):
                if start[0] + i < n and start[1] + i < m:
                    arr.append(mat[start[0] + i][start[1] + i ])
                    
            arr.sort()
            for i in range(len(arr)):
                mat[start[0] + i][start[1] + i] = arr[i]
                
        return mat