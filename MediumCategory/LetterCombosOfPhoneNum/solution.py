class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        phone = {
            '2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        } 
        result = []
        path = []       

        #generate a cartesian product using a dfs
        def dfs(i):
            #end dfs
            if i == len(digits):
                result.append(''.join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                dfs(i+1)
                path.pop()
        dfs(0)

        return result
