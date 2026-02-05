class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #yipee dp, dict to store vale, solution pairings
        memo = {}

        def dfs(amountLeft):
            #base case, amount left is 0 so you reached target
            if amountLeft == 0:
                return 0

            if amountLeft < 0:
                return -1

            if amountLeft in memo:
                return memo[amountLeft]

            #so min works as intended 
            minCost = float('inf')

            for coin in coins:
                res = dfs(amountLeft - coin)
                if res != -1:
                    #add 1 to res since that meant coin counter went up
                    minCost = min(minCost, 1 + res)
            #store
            if minCost != float('inf'):
                memo[amountLeft] = minCost
            else:
                #res must have been -1, store -1
                memo[amountLeft] = -1
            
            return memo[amountLeft]

        return dfs(amount)
