class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #4 sum modification, start with 1 pointers already, then within that we add a 3sum approach for each 4 sum. solution is n^3
        nums.sort()
        result = []
        
        def sum3(currentNum):
            for i in range(currentNum + 1, len(nums) -2):
                #skip only if its not the first index in the loop
                if i > currentNum + 1 and nums[i] == nums[i-1]:
                    continue
                
                left, right = i + 1, len(nums) - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[currentNum]

                    if total == target:
                        result.append([nums[i], nums[left], nums[right], nums[currentNum]])

                        #skip any more dupes since we cant resue them
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        #move them after skipping dupes
                        left += 1
                        right -= 1
                
                    #conditions on how to move left and rigght
                    elif total > target:
                        right -= 1
                    else:
                        left += 1

        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            sum3(i)
        
        return result
