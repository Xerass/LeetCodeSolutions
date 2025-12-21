import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #classical two pointer one for both ends, move both forwaard only if they are  ==, if they cross it must mean it is a palindrome
        #lower to avoid case issues
        s = s.lower()
        #regex away all the non alphanumeric stuff
        s = re.sub(r'[^a-z0-9]', '', s)
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                print(f"char of i:{s[i]}")
                print(f"char of j:{s[j]}")
                return False
        
        return True
