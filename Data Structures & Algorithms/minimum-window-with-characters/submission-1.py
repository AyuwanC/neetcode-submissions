
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        freq_t = defaultdict(int)
        for c in t:
            freq_t[c] += 1

        freq_s = defaultdict(int)
        need = len(freq_t)
        have = 0

        left = 0
        min_len = float("inf")
        start_idx = 0

        for right, c in enumerate(s):
            freq_s[c] += 1

            if c in freq_t and freq_s[c] == freq_t[c]:
                have += 1

            while have == need:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    start_idx = left

                left_char = s[left]
                freq_s[left_char] -= 1

                if left_char in freq_t and freq_s[left_char] < freq_t[left_char]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start_idx:start_idx + min_len]