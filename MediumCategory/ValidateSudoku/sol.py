class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #we know dim is 9x9

        #instead of going over it 1 by 1 per col, row, block
        #we can instead utilize specialized "keys"
        #so instead of checking if 1 exists in this row
        #we instead store (2, 1) to show row 3, has 1.

        #the logic applies to cols as well
        #since we already used the (row / col, number) format
        #to avoid overlap with row keys we go for (num, row/col)

        #next are blocks, blocks can be given by row // 3 and col // 3
        #we store num

        exists = set()
        for row in range(9):
            for col in range(9):
                num = board[row][col]

                #only execute following stuff if num is found
                if num == '.':
                    continue

                #create our tuple keys
                row_key = (row, num)
                col_key = (num, col)
                block_key = (row//3, col//3, num)

                #check if any of those exist in the set
                if col_key in exists or block_key in exists or row_key in exists:
                    return False
                
                #else, we store them
                exists.add(row_key)
                exists.add(col_key)
                exists.add(block_key)

        return True
