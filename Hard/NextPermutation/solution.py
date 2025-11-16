class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #moving from the right, we keep comparing pairwise until it stops ascending, from there we take that as a "pivot" and swap it with the rightside value from it that is the least of the greater values. then we reverse the ordering from the right side to get smallest perm"

        n = len(nums)
        if n <= 1:
            return 
        i = n - 2
        
        #compare pauirs, move if conditions are not met
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1
        
        #if it exited the loop and is not at an invalid index, it must have met a match
        if i >= 0:
            #start searching from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            #once loop stops, it must be at the desired digit, swap them
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

        return nums


