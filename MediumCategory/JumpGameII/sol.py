class Solution:
    def jump(self, nums: List[int]) -> int:
        #perform a greedy aproach
        #jump to largest possible value in the range 
        #go there and do it again
        endOfRange = 0
        jumps = 0
        farthest = 0
        for i in range(len(nums) - 1):
            #always update farthest range we can reach
            farthest = max(farthest, i + nums[i])

            #if we reach the end of our current range, that means we jumped, move endOfRange to our farthest point
            if endOfRange == i:
                jumps += 1
                endOfRange = farthest
            #early stop if we already reached it
        
            if endOfRange >= len(nums) - 1:
                return jumps

        return jumps
