class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, current_xor):
            if i == len(nums):
                return current_xor
            exclude = backtrack(i + 1, current_xor)
            include = backtrack(i + 1, current_xor ^ nums[i])
            return exclude + include
        return backtrack(0, 0)