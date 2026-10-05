class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        freq = defaultdict(int)
        max_frequency = 0
        for right in range(len(s)):

            freq[s[right]] += 1
            max_frequency = max(max_frequency, freq[s[right]])
            
            while right - left + 1 - max_frequency > k:
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right-left +1)
        return max_length