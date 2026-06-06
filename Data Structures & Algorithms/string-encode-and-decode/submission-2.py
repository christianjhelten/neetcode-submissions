class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # "3#TET4#TEST" is our input

        res = []
        i=0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            word_length = int(s[i:j])
            word = s[j+1 : j+1+word_length]
            res.append(word)

            i = j+1+word_length

        return res



            


