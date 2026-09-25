class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set_len = len(set(nums))
        if len(nums) > nums_set_len:
            return True
        else:
            return False
