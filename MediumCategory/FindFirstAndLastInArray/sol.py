class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #modify binary search to instead look for leftmost indices where num >= target and another > target
        #this ensures that we actually capture a range instead of 
        #pass a lambda as the predicate function
        def binary_search_leftmost(arr, predicate):
            low, high = 0, len(arr)

            while low < high:
                mid = (low + high) // 2
                #we dont actually care about finding target, just getting a low as close as possible
                if predicate(arr[mid]):
                    high = mid
                else:
                    low = mid + 1
            
            return low
            

        high = binary_search_leftmost(nums, lambda x: x >= target)
        
        #if high didnt move (left at max). or we never found a left == target, faii
        if high == len(nums) or nums[high] != target:
            return [-1, -1]
        
        low = binary_search_leftmost(nums, lambda x: x > target) - 1

        return [high, low]
