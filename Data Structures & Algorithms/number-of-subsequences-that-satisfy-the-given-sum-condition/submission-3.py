class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l <= r:
            minn = nums[l]
            maxn = nums[r]
            if minn + maxn > target:
                r -= 1
            else:
                ans += 2**(r - l)
                l += 1
        return int(ans % (10**9 + 7))