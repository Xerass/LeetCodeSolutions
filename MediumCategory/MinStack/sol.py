class MinStack:

    def __init__(self):
        #2 stack approach one normal stack one min stack
        self.stack = []
        self.minStack = []

    #push and pop MUST maintain the same stack height for sync purposes
    def push(self, val: int) -> None:
        #push normally for normal stack
        self.stack.append(val)

        #but for min stack, we push only if val is smaller than top else push a dupe of min

        if not self.minStack:
            self.minStack.append(val)
    
        #check to see which one is smaller, push that
        elif self.minStack:
            self.minStack.append(min(self.minStack[-1], val))


    def pop(self) -> None:
        #pop both at the same time so height is =
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
