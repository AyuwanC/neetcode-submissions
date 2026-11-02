class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def backtrack(i):
            nonlocal dp
            if dp[i] != -1:
                return dp[i]

            if i == 1:
                return 1
            elif i == 2:
                return 2 
            dp[i] = backtrack(i-1) + backtrack(i - 2)
            return dp[i]
        
        return backtrack(n)