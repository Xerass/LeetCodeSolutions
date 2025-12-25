class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = ((low) + (high - low) // 2)
            
            print(f"Searching num {nums[mid]}")
            if nums[mid] == target:
                return mid
            #must be in the lesser half
            elif nums[mid] > target:
                #move high to element before mid
                high = mid - 1
            else:
                #greater half, move low to element after mid
                low = mid + 1
        
        return -1
