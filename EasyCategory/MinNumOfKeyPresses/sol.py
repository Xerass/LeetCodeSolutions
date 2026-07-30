class Solution:
    def minimumPushes(self, word: str) -> int:
        #get qoutient and remainder
        n = len(word)
        q, r = divmod(n, 8)

        #since we're the ones who map the letters, and each letter only appers once (means a max of 26)
        #we can literally just count len, set the first 8 at oine press, the next 8 at 2 presses, the next at 3, then the last 2 (since 26) at 4

        #at max cost is 56
        #closed calculation version 
        # just 8 (total keys) * sum of nums 1 -> q. then r is simply q + 1 * remainder (since those didnt fit neatly in the 8 key cycles)
        total = 8 * (q * (q + 1) // 2) + r * (q + 1)


        return total
