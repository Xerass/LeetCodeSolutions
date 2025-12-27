class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []

        #push every value, when operator is read, pop 2, first one is right 2nd one is left
        #for every result, push it back to stack, solution is finished when no more chars and only result left in stack
        for char in tokens:
            if char not in operators:
                #not op, push, convert it to int as well
                stack.append(int(char))
            else:
                #pop 2 chars
                right = stack.pop()
                left =  stack.pop()

                if char == "+":
                    stack.append(left + right) 
                elif char == "-":
                    stack.append(left - right)
                elif char == "*":
                    stack.append(left * right)
                elif char == "/":
                    #int forces result to go towards 0
                    stack.append(int(left / right))
        

        return stack[0]
