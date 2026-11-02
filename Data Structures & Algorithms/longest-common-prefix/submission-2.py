class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        same = True
        j = 0
        while same and j<len(min(strs)):
            key = strs[0][j]
            for i in strs:
                if i[j] != key:
                    same = False
                    break
            else:
                j += 1
                prefix+=key
        return prefix
