class Solution:
    #encode it so that the format is len(n)$String $ is a seprator
    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            n = len(string)
            res.append(f"{n}${string}")

        return "".join(res) 

    def decode(self, s: str) -> List[str]:
        #2 pointers, i, j j finds # i goes behind it to find len
        res = []
        j = 0
        i = 0

        while i < len(s):
            j = s.find("$", i)
            
            lenOfStr = int(s[i:j])

            res.append(s[j + 1: j + lenOfStr + 1])

            i = j + lenOfStr + 1

        return res
