class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        #turbo overkill rolling hash sol
        
        #turn the string into ASCII first so we can turn them into ints, this should make comparison O(1)

        lenOfNeedle = len(needle)
        lenOfHay = len(haystack)

        #len on needle was never specified to be smaller than haystack sooo
        if lenOfNeedle > lenOfHay: return -1

        #begin the hashing process
        #base 26 represents digits of the alphabet (this serves as the rollover)
        base = 26
        #mod ensures that digits stay within the integer box
        mod = 2**31 - 1
        #the rolling hash is computed as: hash(s) =  (s[0] * p(n-1) + s[1] * p(n-2) + ... + s[n-1] * p0 ) %mod

        #pre-compute the power: base^(L-1) % mod
        power = pow(base, lenOfNeedle-1, mod)
        
        #converts every char to an int 
        def char_to_int(c):
            return ord(c) - ord('a')

        #calc the inital hashes of the first window for both strings
        nHash = 0
        curHash = 0

        for i in range(lenOfNeedle):
            nHash = (nHash * base + char_to_int(needle[i])) % mod
            curHash = (curHash * base + char_to_int(haystack[i])) % mod

        #check within the first window
        if nHash == curHash:
            #hashes may collide so its still best to compare that slice to needle
            if haystack[0:lenOfNeedle] == needle:
                return 0

        #rolling the window
        #from 1 to lenOfHay - lenOfNeedle + 1
        for i in range(1, lenOfHay - lenOfNeedle + 1):
            #have a char_leaving window and a char entering
            charL = char_to_int(haystack[i - 1])
            charE = char_to_int(haystack[i + lenOfNeedle - 1])

            #rolling
            #1. remove the leading term
            curHash = (curHash - charL * power) % mod
            #2 move left (mult with base)
            curHash = (curHash * base) % mod
            #add new trailing term
            curHash = (curHash + charE) %mod

            #match check
            if curHash == nHash:
                if haystack[i:i + lenOfNeedle] == needle:
                    return i

        return -1        
