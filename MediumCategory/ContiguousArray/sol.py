class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #fundamental point: if num of 0 = num of 1: we know that if we swap all instances of 0 with -1 then sum is 0.
        max_len = 0
        curr_sum = 0
        #default sum of 0, first index -1 (no digits index in yet)
        hashmap = {0:-1}

        #we dont actually need to track if sum is 0, we just need to see the same sum twice, indicating that  no change in value happened between index1 and index2
        for i in range(len(nums)):
            #mapping our 0 to -1
            curr_sum += 1 if nums[i] == 1 else -1

            #we check if sum is currently in hashmap, if so that means that cumulative difference leads back to 0 (no change in value but value already exists in hash means sum of 0)
            if curr_sum in hashmap:
                curr_len = i - hashmap[curr_sum]
                print(f"curr_len = {curr_len}")
                max_len = max(max_len, curr_len) 
            else:
                #not found in dict add it as earliest instance
                #no need to use get, else handles the exclusivity portion
                hashmap[curr_sum] = i
            
        
        
        return max_len
