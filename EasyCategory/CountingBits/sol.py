class Solution:
    def countBits(self, n: int) -> List[int]:
        #we know that for every power of 2, we add that respective count to output[i]
        #the pattern is for each power of 2, for each number less than it, we add the count from 8 positions before.

        #count 0 in it
        dp = [0] * (n + 1)
        offset = 1
        #set a  dict key for easy lookup (since n <= 1000)

        powers = {2, 4, 8, 16, 32, 64, 128, 256, 512}

        #skip 0 obv
        for i in range(1, n + 1):
            if i in powers:
                offset = i
            
            dp[i] = 1 + dp[i - offset]

        return dp
            
