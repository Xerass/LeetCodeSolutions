class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        k = 0
        #py strings are immutable, use a list for now and just do .join to "" later to avoid lots of string concat overhead
        res = []

        while i < len(word1) and k < len(word2):
            res.append(word1[i])
            res.append(word2[k])
            i += 1
            k += 1
        
        while i < len(word1):
            res.append(word1[i])
            i += 1

        while k < len(word2):
            res.append(word2[k])
            k += 1

        return "".join(res)
