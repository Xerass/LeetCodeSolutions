class Solution(object):
    def groupAnagrams(self, strs):
        #our key will be an array, value will be the string, elements inside the key should all have to be anagrams
        counts = {} #(arr[countofchars], strings)

        def countChars(string):
            countOfChars = [0] * 26

            for i,c in enumerate(string):
                #should give the pos in the actual alphabet
                index = ord(c) - ord('a')
                countOfChars[index] += 1

            #return a tuple so it can be a key
            return tuple(countOfChars)

        #iterate over the array this time
        for word in strs:
            key = countChars(word)
            if key not in counts:
                counts[key] = []
            
            #else append
            counts[key].append(word)
        
        return list(counts.values())
