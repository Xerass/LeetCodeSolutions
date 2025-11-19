import heapq
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        sx, sy =  0,0
        tx, ty = rows - 1, cols - 1
        
        #allowed moves are just down or right 
        DIRS = [(1, 0), (0, 1)]

        #intialize distance / cost in this case
        cost_arr = [[float('inf')] * cols for _ in range(rows)]
        cost_arr[sx][sy] = grid[sx][sy]

        #heap contains cost so far and x,y (for now contains only  start)
        heap = [(grid[sx][sy], sx, sy)]
        
        while heap:
            cost, x, y = heapq.heappop(heap)

            if cost != cost_arr[x][y]:
                continue

            if (x,y) == (tx,ty):
                return cost
            
            #generate children/paths
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    new_cost = cost + grid[nx][ny]
                    #replace if better
                    if new_cost < cost_arr[nx][ny]:
                        cost_arr[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))
        #edge case for no costs
        return float('inf')
