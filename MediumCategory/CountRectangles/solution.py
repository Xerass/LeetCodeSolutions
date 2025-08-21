class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        res = 0

        for i in range(m):
            for j in range(n):
                #treat it like a histogram
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
        
            #count submatrices eding at row i
            for j in range(n):
                if heights > 0:
                    min_h = heights[j]
                    k = j
                    while k >= 0 and heights[k] > 0:
                        min_h = min(min_h, heights[k])
                        res += min_h
                        k -= 1
        return res
