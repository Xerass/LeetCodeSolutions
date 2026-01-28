class Solution:
    def longestPalindrome(self, s: str) -> str:
        #store 2 variables pal_start and pal_len
        #pal_start is at one end of the palindrom
        #pal_len is the length of that palindrome

        pal_start = 0
        pal_len = 0

        #do a for loop, within this for loop, for every i expand outwards on both ends
        #keep expanding and adding 2 to curr len, only until characters are no longer matched
        #for even cases start with i, i+ 1
        #for odd, start with i - 1, i + 1
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            #return len
            return right - left - 1

        for i in range(len(s)):
            len_odd = expand(i, i)
            len_even = expand(i, i + 1)

            curr_len  = max(len_odd,len_even)

            if curr_len > pal_len:
                pal_len = curr_len

                #calc start index
                pal_start = i - (pal_len - 1) // 2

        return s[pal_start : pal_start + pal_len]
