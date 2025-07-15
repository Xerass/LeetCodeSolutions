class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #approach with a complement approach
        num_idx  = {}

        for i, num in enumerate(nums):
            #iterate over the nums, each num subtract with target
            complement = target - num

            #if the complement was already in the array then we can stop and return the indices
            if complement in num_idx:
                return [num_idx[complement], i]
            
            #if not found store the num as a key along with its index
            num_idx[num] = i

