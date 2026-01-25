class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = cost[0]
        prev2 = cost[1]


        for i in range(2, len(cost)):
            #we then calc cost of i with the lesser of the 2 before
            cost_curr = cost[i] + min(prev1, prev2)
            #move all pointer values by 1
            prev1, prev2 = prev2, cost_curr
        

        return min(prev1,prev2)
