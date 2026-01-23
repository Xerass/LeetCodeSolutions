class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a dynamic moving window
        #l,r, r moves and checks for char, if char is is in the window, move l till dupe is no longer ther
        #constantly update len if winlen > maxlen

        max_len = 0
        char_set = set()
        l = 0

        for r in range(len(s)):
            
            while s[r] in char_set:
                #remove that char from the set so we can accurately keep track
                char_set.remove(s[l])
                l += 1
            
            #if no dupes just add the char to the set
            char_set.add(s[r])

            #check max len
            max_len = max(max_len, r - l + 1)

        return max_len
