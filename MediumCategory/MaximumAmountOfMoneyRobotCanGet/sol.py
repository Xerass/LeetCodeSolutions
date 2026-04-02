import math

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        #clearly a dynamic array problem
        #deceptively, it seems like it wants us to use 2 dims since the coins themselves are stored as such
        #the problem with that is we cannot exactly track how many defenses we used (max of 2)

        #this leads us to utilize a graph called dp[i][j][k] where we traverse 3 dimensions at the same time
        #we either move right, down, or we can defend (if choice is available)

        m, n = len(coins), len(coins[0])
        
        #list comprehension to fill dp[m][n][3], filled with -inf to guarantee all coin counts are taken
        dp = [[[math.inf] * 3 for _ in range(n)] for _ in range(m) ]

        #setup start behavior
        dp[0][0][0] = coins[0][0]

        #simple check if first cell is instantly a robber
        #perfect use for our 3 size 3rd dim, we can store case 1 (1 rob defended)
        if coins[0][0] < 0:
            #immediately defend
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                #skip calc on first cell
                if i == 0 and j == 0:
                    continue
                
                possible_val = coins[i][j]

                #here we perform 2 possible options (either neutralize or dont)
                for k in range(3):
                    #first we get max from top and left (previous tiles)
                    prev_max = -float('inf')

                    #ofc check bounds
                    if i > 0:
                        prev_max = max(prev_max,dp[i-1][j][k])
                    if j > 0:
                        prev_max = max(prev_max,dp[i][j-1][k])
                    
                    #now we can either defend or not (if possible val < 0)
                    
                    #option A, leave it
                    #just the default behavior, take it like a champ
                    if prev_max != math.inf:
                        #if all cells before this were valid, then we fill it with prev_max and coun val
                        dp[i][j][k] = prev_max + possible_val

                    #cases where we can steal: possible_val < 0 AND our k > 0 (were in the part of our dp that catalogues steal attempts) 
                    if possible_val < 0 and k > 0:
                        #here we check previous neutralization attempts on said k
                        prev_defend = -math.inf
                        if i > 0:
                            prev_defend = max(prev_defend, dp[i-1][j][k-1])
                        if j > 0:
                            prev_defend = max(prev_defend, dp[i][j-1][k-1])
                        
                        # ff a valid path exists, check if defending yields a higher total
                        if prev_defend != -math.inf:
                            dp[i][j][k] = max(dp[i][j][k], prev_defend)
        
        #return last cell
        return max(dp[m-1][n-1])
