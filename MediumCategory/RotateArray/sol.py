class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #key solution with O(1) space is something with "reversal"
        #key example k = 2 nums = [1,2,3,4,5]
        #supposed anwer = [4,5,1,2,3]

        #reverse # 1 = [5,4,3,2,1]
        #reverse first k elements [4,5,3,2,1]
        #reverse the rest except first k elements [4,5,1,2,3] <- the answer!
        n = len(nums)
        #for considerations where k > n
        shift = k % n

        #shift by using two pointer approach, start and end swap
        def reverse(array, start, end ):
            #classic py tuple unpacking so no need for temp var
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

        #1st reverse
        reverse(nums, 0, n-1)

        #reverse on first k elements
        reverse(nums, 0, shift-1)

        #reverse on last group of elements
        reverse(nums, shift, n-1)

        return nums
