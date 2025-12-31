class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #COOL XOR TRICK COOL XOR TRICK
        #xor works where if a value is ever XOR'd twice, it gets set to 0.

        #if we XOR each number consecutively, this allows us to find which numer that didnt get XOR'd that's the answer
        #since every other num appears twice

        #build the eq: n^n^x^x^a^z^z ... in which a would be left since everything else was a dupe
        result = nums[0]
        for num in nums[1:]:
            result = result^num
        
        return result
