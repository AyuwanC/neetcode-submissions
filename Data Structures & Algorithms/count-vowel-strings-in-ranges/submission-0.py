class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        leftsum = 0
        vowels = ('a', 'e', 'i', 'o', 'u')
        left = [0]
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                leftsum += 1
            left.append(leftsum)
        ans = []
        for l, r in queries:
            ans.append(left[r + 1] - left[l])
        return ans
