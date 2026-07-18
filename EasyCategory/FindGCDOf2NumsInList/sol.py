class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #seems rather literal, just min max and get the gcd
        a = min(nums)
        b = max(nums)

        #euclidian algoritm
        while a != 0:
            mod = b % a
            a, b = mod, a

        res = b

        return res
