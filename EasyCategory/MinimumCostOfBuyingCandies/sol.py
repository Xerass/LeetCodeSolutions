class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        #problem is simple, every 3 items, one is freem the free one can NEVER
        #be greater than the minimum of the other 2. 
        #this means we want to make free the 3rd nost expensive item
        #then the 6th etc.....
        #so long as its i%3 == 0, we can get something for free, and as much as possible
        #free should be max

        #a very intuitive solution that matches our plan is sorting it descending
        #ever 3rd ... will be the free one and guaranteed max

        final_cost = 0
        cost.sort(reverse = True)

        for n in range(len(cost)):
            #ero indexed so 3rd is actually 2, 6th is actually 5th and so on...
            if n%3 == 2:
                #free so we skip
                continue
            final_cost += cost[n]
        
        return final_cost
