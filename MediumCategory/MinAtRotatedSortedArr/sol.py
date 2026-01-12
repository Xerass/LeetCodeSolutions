class Solution:
    def findMin(self, nums: List[int]) -> int:
        #modifed bin search, we know that with the 3 pointers, l, r, mid at least two of them will always be in the "sorted" portion of the array/
        #with that we can determine if mid < r then range is between mid -> r but if left < mid then that means the range is within left -> then we search the opposite one since it means min is within the other range.
        left = 0
        right= len(nums) - 1

        #what were trying to do is find an "inflection" point where the rotation began and simply look to the right of it for the minimum element
        while left < right:
            mid = left + (right - left) // 2

            #typically mid is always < right in a non rotated array, this is a clear sign there was a rotation somewhere here
            if nums[mid] > nums[right]: 
                left = mid + 1
            #otherwise, the sorted part of the array is in the other half
            else:
                #no + 1 sine right being less than has the chance of being min
                right = mid

        return nums[left]
