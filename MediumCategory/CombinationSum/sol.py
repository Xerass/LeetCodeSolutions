class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        #we can use backtracking and pruning candidates based on if their val > remaining.

        results = []
        #sort so we know each val is increasing
        candidates.sort()
        stack = []

        #from here we build the backtrack func
        def backtrack(remaining, stack, start):
            #create the basecase for the recursion
            if remaining == 0:
                #append whatever stack had to res
                results.append(list(stack))
                #no need for any returns
                return
            
            if remaining < 0:
                #failed case, return
                return
            

            for i in range(start, len(candidates)):

                #prune check, since we sorted it, if curr[i] is greater than rem, then no point in trying to add any more, so just return
                if candidates[i] > remaining:
                    return
                
                #append to the stack
                stack.append(candidates[i])

                #pass the state to the next call for their tries on the current state
                #note, we call i and not i+1 because we can reuse the same values over and over
                #we also add the actual "subtraction" step, we dont want to store it in the current state as it already "took" the candidate we want to pass
                backtrack(remaining - candidates[i], stack, i)
    
                #for the remainder of possible vals, we need to "clean" the stack after a backtrack finishes, pop whatever value is at the top, since that will recursively drain the stack back to where it "started"      
                stack.pop()
        
        backtrack(target, stack, 0)
        return results
