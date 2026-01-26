class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #Explicit handling for small arrs
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        #create a 2 pointer solution while creating a dp array to store results
        #rob2 must be max of rob1,rob2 since we can always steal from rob1
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        #starting from second we eval max(rob1 + i, rob2)
        #then we store that max at i
        #then move everything by 1
        #value at last i must be max
        #no need to build an actual arr, we can just store last 2
        for i in range(2,n):
        
            curr_max = max(nums[i] + rob1, rob2)

            #move all by one
            rob1 = rob2
            rob2 = curr_max

        return rob2
