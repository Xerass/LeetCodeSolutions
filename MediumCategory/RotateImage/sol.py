class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #classic solution of transpose eveything, then reverse every row
        n = len(matrix)
        for i in range(n):
            #j denoted from i to n instead of 1
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        #moving from there, we revese on a row wise level
        for i in range(n):
            matrix[i].reverse()
