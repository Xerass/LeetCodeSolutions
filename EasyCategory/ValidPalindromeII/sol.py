import re
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #similar solution to valid palindrome but with the addded step of "if fail, check remaining to see if palindrome still."
        def PalindromeCheck(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True


        s = s.lower()
        s = re.sub(r'[^a-z0-9]','',s)
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                #this is where stuff happens perform a palindrome check with either i or j removed
                return PalindromeCheck(i + 1, j) or PalindromeCheck(i, j - 1)
        
        return True
