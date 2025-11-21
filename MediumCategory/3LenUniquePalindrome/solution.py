class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        #utlize string method find to locate last and first instances of a char
        unique_chars = set(s)
        count = 0
        for char in unique_chars:
            left = s.find(char)
            right = s.rfind(char)

            if left < right:
                #get the middle chars
                mid = s[left+1:right]
                unique_mids = len(set(mid))
                count += unique_mids
        
        return count
