class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #manachers algorithm approach
        
        #for cases of empty string
        if not s:
            return ""

        transform = '#' + '#'.join(s) + '#'
        n = len(transform)
        P =[0] * n 
        center = right = 0

        for i in range(n):
            mirror = 2 * center - i #mirror i around the center

            if i < right:
                P[i]  = min(right - i, P[mirror])

            #expand around i
            a = i + P[i] + 1
            b = i - P[i] - 1
            while a < n and b >= 0 and transform[a] == transform[b]:
                P[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary if expanded past right
            if i + P[i] > right:
                center = i
                right = i + P[i]
