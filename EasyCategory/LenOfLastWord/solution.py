class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        stripped = s.rstrip()
        n = len(stripped)
        count = 0
        i = len(stripped) - 1

        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        
        return count
