class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = defaultdict(int)
        for i in t:
            freq_t[i] += 1
        need = len(freq_t)
        freq_s = defaultdict(int)
        left = 0
        have = 0
        ans = ""
        for right in range(len(s)):
            c = s[right]
            freq_s[c] += 1
            if c in freq_t and freq_t[c] == freq_s[c]:
                have += 1
            while have == need:
                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left:right+1]
                freq_s[s[left]] -= 1
                if s[left] in freq_t and freq_s[s[left]] < freq_t[s[left]]:
                    have -= 1

                left += 1
        return ans
