class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #3 sum is just an extra step 2 sum
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i-1]:
                #duplicate skip
                continue
            
            #this serves as an "anchor" after this we just do a normal 2 sum
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currSum =  nums[i] + nums[left] + nums[right]
                if currSum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    #skip left dupes
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif currSum < 0:
                    left += 1
                else:
                    right -= 1

        return res
        
