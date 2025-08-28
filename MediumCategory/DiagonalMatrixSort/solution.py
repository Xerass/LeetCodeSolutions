from collections import defaultdict, deque

class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid)
        diags = defaultdict(list)


        for i in range(n):
            for j in range(n):
                diags[i - j].append(grid[i][j])


        for k, arr in diags.items():
            if k >= 0:          
                arr.sort(reverse=True)   
            else:              
                arr.sort()              
            diags[k] = deque(arr)       

        for i in range(n):
            for j in range(n):
                grid[i][j] = diags[i - j].popleft()

        return grid
