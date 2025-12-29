from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #create a visited set to store (row, col) tuples so our bfs does not need to iter again
        visited = set()
        islandCounts = 0

        def bfs(row,col,grid):
            #create a q with the starting node in it
            queue = deque([(row,col)])

            #from there while queue is not empty do the entire push thing
            rows = len(grid)
            cols = len(grid[0])
            
            while queue:
                #pop the 1st element
                currRow, currCol = queue.popleft()

                #4 cardinal directions
                dirs = [(0,1), (0,-1), (-1,0), (1,0)]

                #for each tuple, 
                for dx, dy in dirs:
                    newX, newY = currRow + dx, currCol + dy

                    #eval, if valid then add to queue else
                    if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == "1" and (newX, newY) not in visited:
                        #no need to pass as list since deq already got the list from init
                        queue.append((newX, newY))
                        #mark them as visited as well
                        visited.add((newX, newY))

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i,j,grid)
                    islandCounts += 1
        

        return islandCounts
