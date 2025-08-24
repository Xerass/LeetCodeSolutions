class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #sliding window approach
        left = 0
        zeros = 0
        best = 0

        for right, v in enumerate(nums):
            if v == 0:
                zeros += 1
            #checks to see if zeroes are greater than one and if so if left can move
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            best = max(best, right - left)
        
        return best
