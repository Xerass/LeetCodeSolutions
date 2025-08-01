class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #utilize a stack structure
        stack = []

        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                #pop it from stack if not empty, else give #
                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False
            
            else:
                #must be an opening bracket
                stack.append(char)


        #valid should have an emptyu stack
        return not stack
