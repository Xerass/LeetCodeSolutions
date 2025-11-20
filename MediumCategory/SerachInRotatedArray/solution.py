class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #implement a modified binary serach
        left = 0
        right = len(nums) - 1

        while left <= right:
            #get mid
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            #determine which half was actually moved, go to the non-moved side
            if nums[left] <= nums[mid]:
                #check if target is within the range of this half
                if nums[left] <= target <= nums[mid]:
                    #search in left half 
                    right = mid - 1
                else:
                    left= mid + 1
            else: #(right half was sorted)
                if nums[mid] <= target <= nums[right]:
                    #search in right half
                    left = mid + 1
                else:
                    right = right - 1

        
        #if none were found
        return - 1
