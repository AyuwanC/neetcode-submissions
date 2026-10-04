class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = {}
        n = len(s)
        for right in range(n):
            previous = seen.get(s[right], -1)
            if previous != -1:
                left = max(left, previous + 1)
            seen[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length