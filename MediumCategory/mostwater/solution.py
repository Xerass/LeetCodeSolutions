class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #start with two outer pointers
        left = 0
        right = len(height) - 1
        max_area = 0


        #iterate while moving the pointers
        while left < right:
            h = min(height[left], height[right])
            l = right - left
            area = h * l
            max_area = max(area, max_area)


            #move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
