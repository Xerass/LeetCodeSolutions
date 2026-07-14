class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #they're already in ints so this is just begging for a count-sort
        #but the challenge goes against it since it's a 2-pass
        #we can instead just swap everything around and maintain a low, mid, high  pointers

        #mid is our scanner pointer
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                #swap with low
                nums[low], nums[mid] = nums[mid], nums[low]
                #adnance low and mid at the same time
                low += 1
                mid += 1
            elif nums[mid] == 1: #keep as is, if we move 0 and 2 to the ends we get 1s in the middle anyways
                mid += 1
            elif nums[mid] == 2:
                #swap with high, high decrements
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                #we dont advance high since there are cases where the newly swapped element is still swappable
            
        return nums
