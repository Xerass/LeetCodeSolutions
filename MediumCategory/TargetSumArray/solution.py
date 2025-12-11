class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        dp = {}
        n = len(nums)
        #approach by creating a binary tree with backtracking to get count of total solutions, use dfs for ease.
        #format each node to be a pair of index and total, each split is either a +1 or -1
        def dfs(i, total):
            #once end of arr is reacehed check if total == target
            if i == n:
                if total == target:
                    return 1 #mark as sol
                else:
                    return 0 #not a sol

            #perform some memoization, dp stores the tuple i,total if they are already in there, no need to solve again
            if (i, total) in dp:
                return dp[(i,total)]

            
            #backtrack left is add next to total, right is -  next to total
            dp[(i,total)] = (dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i]))

            #at the end this should give the total nums
            return dp[(i,total)] 

        return dfs(0,0)
