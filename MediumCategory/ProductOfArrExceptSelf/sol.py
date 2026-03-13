class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #build prefix and postfix arrays per index. then multiply each

        #obviously, division is the best choice here but since we cant do that..
        
        arr_len = len(nums)
        #why one? so we can easily multiply digits to it (also default val)
        prefix = [1] * arr_len
        suffix = [1] * arr_len

        for i in range(arr_len):
            #prefix product is just last_prod * prev_num
            if i > 0:
                prefix[i] = prefix[i-1] * nums[i - 1]
        

        #suffix goes from right to left
        for i in range(arr_len - 2, -1, -1):
            if i >= 0:
                suffix[i] = suffix[i+1] * nums[i+1]

        print(prefix)
        print(suffix)

        result = [1] * arr_len
        for i in range(arr_len):
            #ok, now we multiply per index
            result[i] = suffix[i] * prefix[i]


        return result
