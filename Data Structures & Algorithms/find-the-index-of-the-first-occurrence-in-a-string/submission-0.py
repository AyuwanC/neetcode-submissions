class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    break
                else:
                    occ = i
            else:
                return occ
        return -1

