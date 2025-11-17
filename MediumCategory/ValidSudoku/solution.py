class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #utilize a similar bit mask approach to the sudoku solver
        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9

        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

        #iterate over the board and keep track, if any same appears 
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                ch = board[r][c]
                # convert char '1'..'9' to bit (1<<0 .. 1<<8)
                d = ord(ch) - ord('1')     # 0..8
                bit = 1 << d
                b = box_index(r, c)

                #check if they are already in any of the cells considered
                if (row_mask[r] & bit) or (col_mask[c] & bit) or (box_mask[b] & bit):
                    return False

                #set the bit
                row_mask[r] |= bit
                col_mask[c] |= bit
                box_mask[b] |= bit

        return True
