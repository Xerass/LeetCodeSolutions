class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #utilize a DFS and bitmasking

        ALL = (1 << 9) - 1 # should be 0b111111111

        #apply masks
        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9
        empties = [] # list of coords

        def box_index(r, c):
            return (r//3) * 3  + (c//3)

        #initialize a mask and empties
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r,c))

                else:
                    d = int(val) - 1
                    bit = 1 << d
                    row_mask[r] |= bit
                    col_mask[c] |= bit
                    box_mask[box_index(r, c)] |= bit
        
        #bit counter
        def popcount(x):
            count = 0
            while x:
                x &= x - 1
                count += 1
            return count
        
        #recursion with minimum remaining values heuristic

        def dfs():
            if not empties:
                return True #no more empites, thus solved
            
            #choose an empty cell with as few possible candidates
            #edfault vals
            best_idx = -1 
            best_count = 10
            best_cands = 0

            #scan empties to find MRVs
            for i, (r,c) in enumerate(empties):
                #utliize masking to quickly evaluate
                used = row_mask[r] | col_mask[c] | box_mask[box_index(r,c)]
                cands = ALL & ~used
                pop = popcount(cands)
                if pop == 0:
                    return False #deadend
                if pop < best_count:
                    best_count = pop
                    best_idx = i
                    best_cands = cands
                    if pop == 1:
                        break #one is already optimal choice
            r,c = empties.pop(best_idx)
            b = box_index(r,c)

            #iterate over candidate bits, go for lowest bit first
            cand = best_cands
            while cand:
                bit = cand & -cand
                cand -= bit
                d = (bit.bit_length() - 1)  # 0..8
                
                # place digit (d+1)
                board[r][c] = str(d+1)
                row_mask[r] |= bit
                col_mask[c] |= bit
                box_mask[b] |= bit
                
                if dfs():
                    return True
                
                # backtrack
                board[r][c] = '.'
                row_mask[r] &= ~bit
                col_mask[c] &= ~bit
                box_mask[b] &= ~bit
            # restore empties list (put cell back)
            empties.insert(best_idx, (r, c))
            return False
    
        dfs()
        return
