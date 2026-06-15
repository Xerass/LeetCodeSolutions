class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sorting it makes pruning a lot easier
        candidates.sort()

        result = []


        #backtracking, take, if remaining is less than next prune branch
        #else if start and candidates[i] == candidates[i-1] skip (dedup)
        #if is passes through we recurse with i + 1, remaining - candidates[i]

        #combo is the current sequence of "takes", a list
        def backtrack(start, combo, remaining):
            if remaining == 0:
                #slicing makes sure it creates a new list instead of attaching a pointer
                result.append(combo[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if remaining < candidates[i]:
                    break
                
                combo.append(candidates[i])
                backtrack(i + 1, combo, remaining - candidates[i])

                #pop latest append to simulate not taking candidate
                combo.pop()
        
        backtrack(0, [], target)
        
        return result
