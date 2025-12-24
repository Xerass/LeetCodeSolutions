class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #store a max 
        maxArea = 0
        i = 0
        j = len(heights) - 1

        #move two pointers calc area each time, whichever is the smaller is the one we move
        #since there may be a chance we find one bigger that can fit more water
        #while doing that store a max, so we can constantly update it
        while i < j:
            area = (j - i) * (min(heights[j], heights[i]))
            print(area)
            if area > maxArea:
                maxArea = area
            
            if heights[j] > heights[i]:
                #i is smaller move i
                i += 1
            else:
                j -= 1
        
        return maxArea
