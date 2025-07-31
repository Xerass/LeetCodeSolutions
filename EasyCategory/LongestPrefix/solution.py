class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # start with the first string as the initial prefix
        prefix = strs[0]

        for i in strs[1:]:
            #iteratively remove characters from each string til  they all match
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
