class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #we do this in a 2 step process done in actual linear algebra
        #to rotate a matrix 90 degreesm we first need to transpose mat[i][j] = mat[j][i]
        #then we reverse each row 
        n = len(matrix) #sqyare so we only need one

        def reverse(arr):
            i = 0
            j = len(arr) - 1

            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        #transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

        #then we reverse it row wise
        for i in range(n):
            reverse(matrix[i])
