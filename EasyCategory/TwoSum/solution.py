class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {} #value and index keys
        n = len(nums)

        #perform a complement check we understand that target - num1 = num2
        #we know target so just find the num2 given respective nums[i]
        #if in arr then that must be a solution else search
        #store complement existence in arr so we no longer need to check numbers over and over
        for i in range(n):
            difference  = target - nums[i]

            #difference exists in maps must mean it is the solution
            if difference in maps:
                return [maps[difference], i]

            maps[nums[i]] = i 
            
