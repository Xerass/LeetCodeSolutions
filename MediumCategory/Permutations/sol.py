class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking, classical
        #one path take, one path dont take, one path for EACH possible input
        #len is only 6 so the expected complexity of n! is fine
        result = []

        #tracks current path
        path = []
        used = [False] * len(nums)
        
        #the algorithm is simple, just insert one num, pass it to backtrack mark it as used
        #then pop it, unmark it, then another run

        def backtrack():
            #maxed out, new perm
            if len(path) == len(nums):
                result.append(path[:]) #slice to create a snapshot of res since path unsliced hands over the exact same list, not a copy
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
            
        backtrack()
        return result
