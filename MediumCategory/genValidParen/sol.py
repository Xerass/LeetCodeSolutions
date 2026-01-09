class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtrack, only add openers if < n only add closers if < openers and < n

        res = []
        maxLen = 2 * n

        def paren(currStr: str, openCount: int, closeCount: int):
            #base case, if len of str is max then k paren is complete
            if len(currStr) == maxLen:
                res.append(currStr)
                return
            
            if openCount < n:
                paren(currStr + '(', openCount + 1, closeCount)
            #no need to check for n since open count does this already
            if closeCount < openCount:
                paren(currStr + ')', openCount, closeCount + 1)
            
        paren("", 0, 0)
        return res
