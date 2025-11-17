class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        #most base term
        string = "1"
        for j in range(2, n + 1):
            result = []
            i = 0
            L = len(string)

            while i < L:
                count =  1
                current_char = string[i]

                while(i + count < L) and (string[i + count] == current_char):
                    count = count + 1

                #append count and char to res
                result.append(str(count))
                result.append(str(current_char))

                i = i + count #mvoe to next char

            string = "".join(result)
        
        return string

