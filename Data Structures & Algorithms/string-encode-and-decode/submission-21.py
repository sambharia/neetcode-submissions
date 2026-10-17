class Solution:

    # strs = ["Hello","World"]
    def encode(self, strs: List[str]) -> str:

        output = ""
        for s in strs:
            output = output + str(len(s)) + "#"  + s

        return output

        
        # output = 5#Hello5#World3#new
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res