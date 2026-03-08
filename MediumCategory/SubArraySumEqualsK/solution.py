class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #approach with hashmaps
        #we know that if we keep a running currentSum 
        #if we find a case such that currentSum - previousSum = K, then we would have known that that range of values up to that point MUST have added up to K.
        
        #keeps count of viable solutions
        count = 0
        curr_sum = 0

        #default hash, to set this up properly, we know that we have found 1 solution where sum is  0 (one with no input yet)
        hashmap = {0:1} #sum : frequency

        for num in nums:
            #running sum
            curr_sum += num

            #with current sum we know that to find a subarray summing to  k say in this case sum = 12 k = 3, if we know that the previous sum IS 9 then that must mean from this point to that point, we found a subarray that = k.
            diff = curr_sum - k
            #check if diff already exists in our dict
            if diff in hashmap:
                #add the frequency of that to count
                #we add frequency because it counts how many times that sum occured BEFORE we reached the = diff, since subarrays can start multiple times from that point
                count += hashmap[diff]
            
            #then we add the current_sum to the hashmap
            hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1

        return count
