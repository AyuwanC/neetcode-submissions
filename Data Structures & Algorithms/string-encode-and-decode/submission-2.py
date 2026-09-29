class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + ',' + i
        return s
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        
        while i < len(s):
            comma = s.find(',', i)
            n = int(s[i:comma])
            strs.append(s[comma+1:comma+1+n])
            i = comma + n + 1
        return strs
