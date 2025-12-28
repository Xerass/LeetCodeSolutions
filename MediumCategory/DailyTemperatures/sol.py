class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        #starting from 0 we push indices one by one, if we push and look at top and push > top then we calc difference in their index.
        #perform the first push
        if not stack:
            stack.append(0)

        for i in range(1,len(temperatures)):
            #compare temps of curr to temp of top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                print(f"curr i {i}, curr comps {temperatures[i]} > {temperatures[stack[-1]]}")
                print(f"curr op {i} - {stack[-1]}")
                print(f"stored result: {i - stack[-1]}")
                #find them difference between indices and store that
                prev = stack.pop()
                result[prev] = i - prev 
            stack.append(i)

        return result
