class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #in place, change everry row and col where there is a 0 into 0
        #we can abuse the outer col and row (row 0, col 0) as "sentinels" where 0 marks in them means
        #this entire row / col is going to get 0

        rows = len(matrix)
        cols = len(matrix[0])

        #since we're essentially polluting the information in row 0 col 0, we need to first know if
        #there are any 0s in them to preserve that information
        first_row_has_zero = any(cell == 0 for cell in matrix[0])
        first_col_has_zero = any(row[0] == 0 for row in matrix)
        
        #updated to use faster checks than earlier one by one checks, fundamentally the same algorithm though
        
        #first pass, investigate all zeroes.
        for r in range(1, rows):
            if 0 in matrix[r]: #C-speed scan, usually rejects the row instantly, after that all we need to check is col
                for c in range(1, cols):
                    if matrix[r][c] == 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        #second pass is application
        for r in range(1, rows):
            if matrix[r][0] == 0:
                matrix[r][1:] = [0] * (cols - 1)# one C-level slice assignment
            else:
                for c in range(1, cols):
                    if matrix[0][c] == 0:
                        matrix[r][c] = 0
                

        if first_row_has_zero:
            matrix[0][:] = [0] * cols
        
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
