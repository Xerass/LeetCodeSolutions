class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {   "{":"}",
                    "(":")",
                    "[":"]"}

        stack = []

        #create a set of the closers as we will use pair dict to look up for keys (openers)
        closers = set(pairs.values())

        for char in s:
            if  char in pairs:
                #append is the "push"
                stack.append(char)
            if char in closers:
                #is a closer so we need to check if a pop matches it, else false
                #stack empty but char was still read, must mean excess
                if not stack:
                    return False
        
                #pop a char from the stack, if it is not within the pairs invalid
                evalChar = stack.pop()

                #if the opener (the ones we push to stack) does not match the closer, false
                if pairs[evalChar] != char:
                    return False
        
        #if it passes the loop, must mean it is valid (check if empty first tho)
        return not stack
