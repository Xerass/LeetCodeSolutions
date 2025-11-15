class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #since we only care about positive digits, we can effectively ignore all negatives,
        #we try to place nums[i] say 3 at its "correct" index of 3.
        #we swap any digit to thier correct index and skip if negative
        #after this, we check the modified array and see if nums[i] + 1 = nums[i+1] if not, it must be smallest positive
        i = 0
        n = len(nums)
        while i < n:
            v = nums[i]
            #check if its within range and if its already in it's correct spot, else swap.
            if 1 <= v <= n and nums[v - 1] != v:
                nums[i] = nums[v-1]
                nums[v-1] = v
                #we dont increment i, as we recheck it 
            else:
                i = i+1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        #if no missing, earliest missing positive will be len +  1
        return n + 1

        
