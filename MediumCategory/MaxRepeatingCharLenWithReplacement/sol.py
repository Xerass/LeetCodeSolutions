class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        state = {} #going to be a frequency map of each char within the window

        #len for result, frequency to track who will be the "basis" of the strings
        max_len = 1
        max_freq = 0

        #we use for loop on right, to easily handle cases where a right mighht not exist or is out of bounds
        for right in range(len(s)):
            #update state dict. use get for safety
            state[s[right]] = state.get(s[right], 0) + 1

            #reference max_freq, see if s[right] letter count exceeds current max, if so we use that as basis
            #we dont need to know the letter, just how many exist in the window so we know how many we can replace
            max_freq = max(max_freq, state[s[right]])

            #we also dont even need to know the specific counts of each letter
            #we know that len = max_freq_letter + leftovers, if leftovers > k that means we cant replace them all
            #thus window is invalid
            leftovers = (right - left + 1) - max_freq

            if k < leftovers:
                #window is invalid, we then move left side
                state[s[left]] -= 1
                left += 1

            #else, we move on and see if current len is > max_len
            max_len = max(max_len, (right - left + 1))
        
        return max_len
