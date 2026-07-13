class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        #the pattern is apparent, say range is 1 -> 2000, we know that we can build sequences of length 2 -> 4.
        #there's also an apparent pattern: 12, 23, 34, 56, 78, 123, 234
        #so a "brute forced" soltion would be to list out all 5 possibliites for the 9 spaces
        #we can also create a builder, who'll run at a max of 40 iterations

        #lets do that

        candidates = "123456789"
        result = []

        #it's a double loop so it looks like it's n2 but its actually just O(36) since there are only
        #36 possible slides this iterates over
        for i in range(2, 10):
            #only move up to what Left can allow
            for j in range(0, 10 - i):
                #take the window from j to max range
                window = candidates[j : j + i]
                num = int(window)
                if low <= num <= high:
                    result.append(num)

        return result
