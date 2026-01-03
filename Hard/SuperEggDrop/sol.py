class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        #after aggressively trying to figure out how triangle numbers somehow fit into this, i later realized they are literally just patterns, anyways, dynamic programming time.

        #didnt figure this out on my own but the intuition is neat

        #2d arr with egg (k) cols and n(floor) rows (this is mostly for k = 1) where everuthing is linear.
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        #the table is gonna look like: moves K0 | k1 | k2 | k3 then we fill up the value of the 2 adjacent nodes based on prev values of dp[m-1][k-1] and dp[m-1][k] + 1

        #where did we get that? both of the values in the addition is a scenario where the egg breaks or not and our current move budget, dp[m-1][k-1] represents previous move with one less egg, while dp[m-1][k] represents previous move budget  without the egg breaking. the + 1 at the end is the floor you dropped the egg at (since its techincally still part of the budeget)

        #this builds up a table of moves and our move budget for each value, we return the value of move where the budget exceeds n (floors).

        #we literally just ignore the floors and just wait till the move budget exceeds the floor, which gives a guarantee. We dont need to simulate actually finding a value in range n and figuring out mvoes from there, we just need to consider how many more tries we have left if an egg breaks or not after dropping it. 

        #so for example, our move budget for n = 1 is 1 for all k's since we can only ever drop it 1 time.
        #but for floor 3, k = 2 ; we can see that m2,k1 will now hold value 2 since prev values were 1 and 1 then for k2 it's 3 since adjacent 

        #more visually understandable:
        #m = 0: [0,  0,  0,  0]  
        #m = 1: [0,  1,  1,  1]  
        #m = 2: [0,  2,  3,  3]  
        #m = 3: [0,  3,  6,  7]  
        #m = 4: [0,  4, 10, 14]  
        
        #hey it looks like the solution to the knapsack problem

        #anyways, solution is really short
        
        #while move budget at optimal egg count (current max eggs) is less than floor len
        m = 0
        while dp[m][k] < n:
            m+=1
            #fill up the values for each k
            #we dont fill up 0 though so start at 1 to k + 1 (where the last k should be)
            for i in range(1, k+1):
                dp[m][i] = dp[m-1][i - 1] + dp[m-1][i] + 1

        #you can probably optimize this more by only storing the row before m but i like the 2d represenation more, feels more intuitve
        return m


