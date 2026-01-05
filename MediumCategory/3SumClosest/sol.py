class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #average 3 sum sol but target is now +- target

        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        #stop at -2 since we need 3 elements 
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                #check if greater than closestSum but less than target
                #use absolute difference 
            
                if abs(closestSum - target) > abs(currentSum - target):
                    print(f"Replaced {closestSum} with {currentSum}")
                    closestSum = currentSum

                #move pointer pased on value
                if currentSum > target:
                    right -= 1
                else:
                    left += 1
        
        return closestSum
