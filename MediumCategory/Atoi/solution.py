class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i, n = 0, len(s)

        while i < n and s[i].isspace():
            i += 1
        if i == n:
            return 0
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        res = 0
        ord0 = ord('0')
        limit10_pos, cutoff_pos = INT_MAX // 10, 7   
        limit10_neg, cutoff_neg = (-INT_MIN) // 10, 8 

        while i < n:
            d = ord(s[i]) - ord0
            if d < 0 or d > 9:
                break

            if sign == 1:
                if res > limit10_pos or (res == limit10_pos and d > cutoff_pos):
                    return INT_MAX
            else:
                if res > limit10_neg or (res == limit10_neg and d > cutoff_neg):
                    return INT_MIN

            res = res * 10 + d
            i += 1

        return res if sign == 1 else -res
