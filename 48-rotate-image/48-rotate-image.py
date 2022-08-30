class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range((n+1)//2):
            for j in range((n+1)//2):
                if i*2 != n-1:
                    a = matrix[i][j]
                    b = matrix[j][n-1-i]
                    c = matrix[n-1-i][n-1-j]
                    d = matrix[n-1-j][i]
                    
                    
                    matrix[i][j] = d
                    matrix[j][n-1-i] = a
                    matrix[n-1-i][n-1-j] = b
                    matrix[n-1-j][i] = c