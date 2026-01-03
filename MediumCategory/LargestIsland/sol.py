from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #a similar solution to numIslands can be used, with an added step of tracking total no. of 1s visited
        #so that we can count the actual area

        visited = set()
        largestIsland = 0

        def bfs(row,col,grid) -> int:
            q = deque([(row, col)])
            #add this since cases can happen where island size = 1
            visited.add((row, col))
            area = 1

            
            rows = len(grid)
            cols = len(grid[0])

            while q:
                cRow, cCol = q.popleft()
                #4 card dirs
                dirs = [(0,1), (0,-1), (1,0), (-1,0)]

                for dx, dy in dirs:
                    nX, nY = cRow + dx, cCol + dy

                    #eval 4 dirs, if valid add to q, else dont
                    if 0 <= nX < rows and 0 <= nY < cols and grid[nX][nY] == 1 and (nX, nY) not in visited:
                        #append to q
                        visited.add((nX, nY)) 
                        q.append((nX, nY))
                        area += 1
            
            return area

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and (x,y) not in visited:
                    area = bfs(x,y,grid)
                    print(f"curr area{area}")
                    largestIsland = max(largestIsland, area)

        return largestIsland
