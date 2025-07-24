class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        previous = 0

        for i in reversed(s):
            value = roman_map[i]
            
            if value < previous:
                total -= value
            else:
                total += value

            previous = value

        return total
