class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #same solution, just split between using last node or first node as start
        #max whatever result 
        n = len(nums)
        #Explicit handling for small arrs
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        #starting from second we eval max(rob1 + i, rob2)
        #then we store that max at i
        #then move everything by 1
        #value at last i must be max
        #no need to build an actual arr, we can just store last 2
        def rob(houses):
            rob1,rob2 = 0,0
            for nums in houses:
                curr_max = max(nums + rob1, rob2)

                #move all by one
                rob1 = rob2
                rob2 = curr_max
            
            return rob2

        #operate on 2 slices, 0 - n-1 (excluding last) and 1 - n (excluding first)
        return max(rob(nums[:-1]), rob(nums[1:]))
