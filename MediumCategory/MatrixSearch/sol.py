class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #have 2 binary searches
        #one binary search will determine the row, the other is the typical one
        m = len(matrix)
        #catch case where its actually just a 1d array
        n = len(matrix[0]) if m > 0 else 0


        rowLow = 0
        rowHigh = m - 1
        rowToSearch = -1

        while rowLow <= rowHigh:
            mid = rowLow + (rowHigh - rowLow) // 2
            print(f"Row searched rn {mid}")

            if target > matrix[mid][-1]:
                #target is higher than max of that row, move up
                rowLow = mid + 1
            elif target < matrix[mid][0]:
                #target is lower than min of that row move down
                rowHigh = mid - 1
            else: #if both conditions fail, then it must be in that range
                rowToSearch = mid
                break
        

        #now do a normal bin search on that sub arr
        low = 0
        high = n - 1

        if rowToSearch == -1:
            return False

        while low <= high:
            mid = low + (high - low) // 2
            #current values of low
            print(f"current low high {low}, {high}")

            if matrix[rowToSearch][mid] == target:
                return True
            elif matrix[rowToSearch][mid] > target:
                #must be in lower half
                high = mid - 1
            else:
                low = mid + 1
        

        return False
