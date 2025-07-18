class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #performing the sliding window approach
        char_index = {} #stores index of each char
        left = 0 #pointer of the window
        max_length = 0 #keep track of max len

        #iterate over the string
        for right in range(len(s)):
            current = s[right]

            #checks to see if the character ws seen before and is inside the current window
            #if so, we move the left pointer past the last occurence of that char
            #this ensures that it does not duplicate
            if current in char_index and char_index[current] >= left:
                    left = char_index[current] + 1

            
            #update the last seen index for currnet
            char_index[current] = right


            #current window should now be from index left to current right
            window_length = right - left + 1

            max_length = max(max_length, window_length)
        return max_length
        
