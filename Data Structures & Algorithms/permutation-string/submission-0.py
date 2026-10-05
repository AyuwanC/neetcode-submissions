class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        freqs1 = [0 for i in range(26)]
        freqs2_sw = [0 for i in range(26)]
        for i in s1:
            freqs1[ord(i)-ord('a')] += 1
        left = 0
        for right in range(len(s2)):
            freqs2_sw[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 > n:
                freqs2_sw[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if freqs2_sw == freqs1:
                return True
        return False
