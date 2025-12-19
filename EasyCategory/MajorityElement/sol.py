class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we can store a dict of counts and if any number goes above n/2 ut must be a majority element.

        counts = {} #num, count of num
        n = len(nums)

        for i, num in enumerate(nums):
            counts[num] = counts.get(num, 0) + 1

            #.get was already used so this should always be safe
            if counts[num] > (n/2):
                return num
            
