class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        result = 0
        has_odd = False

        for count in counts.values():
            #take all evens
            if count % 2 == 0:
                result += count
            if count % 2 == 1:
                result += count - 1 #take count - 1 to make it even
                has_odd = True 

        #sicne there was an odd, at least one of those we will still be odd in the max, so just add 1 
        if has_odd:
            result += 1

        return result
