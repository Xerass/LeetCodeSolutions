class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if we utilize the typical bin search strat, we end up with a potential situation where left > right. 
        #this means we effectively have 2 sorted segments, the problem is, how do we find the point of rotation.
        #we can do this by setting an l and r bin sort, we get mid, if r < mid left is sorted but if we get l > mid, right part is sorted

        #we can even further simplify this by skipping searching for the cut, we simply check if target falls between
        #the sorted ranges of the 2 halves.

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            #else, we do a check
            
            #see which half is sorted
            if  nums[left] <= nums[mid]:
                #we know left half is sorted. we then check if target is in range
                if nums[left] <= target < nums[mid]:
                    #if so target is in this range, we search left section
                    right = mid - 1
                else:
                    #if not, we go to the left
                    left = mid + 1
            #same logic for right side sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
