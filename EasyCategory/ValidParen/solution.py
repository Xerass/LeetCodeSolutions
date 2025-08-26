class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {')': '(', ']': '[', '}': '{'}
        openings = set(match.values())
        stack = []

        for ch in s:
            if ch in openings:
                stack.append(ch)
            elif ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
        
        return not stack

