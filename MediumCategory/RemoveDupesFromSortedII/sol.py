class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #approach it with a 2 pointer strat
        #writer will write whatever element it needs to
        #a current will check over the entire array to ensure it is safe
        writer = 0

        for current in range(len(nums)):
            #for the first 2 incides, they are always valid since no way count > 2
            #for anything beyond that, we try to check if current is a diff number from nums[writer - 2] if so then we can write it
            if writer < 2 or nums[current] > nums[writer - 2]:
                nums[writer] = nums[current]
                writer += 1
        
        #return k, len of valid indexes (which writer should be at by now)
        return writer
