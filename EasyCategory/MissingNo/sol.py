class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #we can XOR for each nu  on the range, since only one is missing, it must mean we xor each num twice except for the missing num, this should leave value as the missing number
        n = len(nums)
        result = n
        for i in range(n):
            result ^= i ^ nums[i]
        
        return result
