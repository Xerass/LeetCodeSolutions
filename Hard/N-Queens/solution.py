class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #we try to place one queen per row then try to place again at the row below it avoiding tiles where it is attacked by a queen already (covered by bitmask)
        #store cols, diag1,diag2, no need for row as they are placed exclusively to one row each
        #bit mask yet again
        ALL = (1 << n) - 1
        solutions = []
        def build_board(col_indices):
            board = []
            for c in col_indices:
                row = '.' * c + 'Q' + '.' * (n - c - 1)
                board.append(row)
            return board
        #backtracker
        def dfs(row, cols, diagL, diagR, current_pos):
            #if row == n that must mean each queen was successfully placed at their rows without conflict, thus it is a solution.
            if row == n:
                solutions.append(build_board(current_pos))
                return
            
            available = ~(cols | diagL | diagR) & ALL
            while available != 0:
                pos = available & -available  #get the lowest available column bit
                available = available ^ pos #use a xor to "remove" it from available by making said bit false

                col_index = pos.bit_length() - 1 #get the length of the bit (cool quirk but bit_length actually returns HOW many bits are needed to get that digit) and -1 since we use base 0

                current_pos.append(col_index)

                dfs(
                    row + 1,
                    cols | pos,
                    (diagL | pos) << 1,
                    (diagR | pos) >> 1,
                    current_pos
                )

                current_pos.pop()
        dfs(0,0,0,0, [])
        return solutions
