class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft = 0
        sumright = sum(nums) - nums[0]
        n = len(nums)
        if sumleft == sumright:
            return 0
        for i in range(1, n):
            sumleft+= nums[i-1]
            sumright -= nums[i]
            if sumleft == sumright:
                return i
        return -1

