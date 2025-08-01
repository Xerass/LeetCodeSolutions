class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val_to_roman = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I"),
    ]

        result = ""
        #greedy approach

        #iterate over value list
        for val, symbol in val_to_roman:
            #append the largest symbols at all times
            while num >= val:
                #add to result remove from num
                result += symbol
                num -= val

        return result
