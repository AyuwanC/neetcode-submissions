class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j, n = 0, 0, len(s)
        while i < n:
            if not s[i].isalnum():
                i+=1
                continue
            elif not s[n-1-j].isalnum():
                j+=1
                continue
            elif s[i] != s[n-1-j]:
                print(s[i], s[n-1-j])
                return False
            i+=1
            j+=1
        return True