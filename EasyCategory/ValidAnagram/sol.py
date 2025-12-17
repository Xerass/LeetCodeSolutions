class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Scounts = {}
        Tcounts = {}

        sLen = len(s)
        tLen = len(t)
        
        #immediate no
        if sLen != tLen:
            return False

        #build counts dict to compare later
        for i,c in enumerate(s):
            if c in Scounts: 
                Scounts[c] += 1
            else:
                Scounts[c] = 1
        
        #build counts dict for other str 
        for i,c in enumerate(t):
            if c in Tcounts: 
                Tcounts[c] += 1
            else:
                Tcounts[c] = 1
        
        if Tcounts == Scounts:
            return True
        
        return False
