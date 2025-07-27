class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """general rules:
            1. ignore consecutive dupes
            2. if not equal, higher than both neighbors is hill, lower is valley
            3. boundaries are excluded
        """

        filtered = [nums[0]]

        for i in range (1, len(nums)):
            #removes dupes
            if nums[i] != nums[i - 1]:
                filtered.append(nums[i])

        #count hills and valleys
        count = 0
        for i in range (1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1
            if filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1
        return count
