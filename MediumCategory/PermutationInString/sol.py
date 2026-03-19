class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #ok easy check, just a tracking dict
        
        counts = {}

        for char in s1:
            counts[char] = counts.get(char,0) + 1
        
        #now that we have counts, we can easily do a sliding window op
        
        #this also helps us a lot, we know len can never exceed this
        #so what we can do is just set a fixed window size of sublen
        #then move that 1 at a time, if any counts dont match / window is now beyond arr
        #we know no subset exists

        sublen = len(s1)
        left = 0 

        #quick check if sublen is actually > len
        if sublen > len(s2):
            return False
            
        #running frequency counts
        freq = {}

        #fill the first window
        for i in range(sublen):
            freq[s2[i]] = freq.get(s2[i], 0) + 1
        
        #if first window is already a match return true
        if freq == counts:
            return True
        
        #move left and right one at a time, keeping track if any matches occured
        for right in range(sublen, len(s2)):
            added_char = s2[right]
            #we add that to freq
            freq[added_char] = freq.get(added_char, 0) + 1

            #remove from the left to maintain window size
            removed = s2[left]
            #we know left for sure exists so just - 1 no need to get
            if freq[removed] == 1:
                #if its just one remove it from dict entirely
                del freq[removed]
            else: #else just subtract
                freq[removed] -= 1
            
            left += 1

            #check if new window is a match
            if freq == counts:
                return True
        

        #if we somehow get here, its false
        return False
