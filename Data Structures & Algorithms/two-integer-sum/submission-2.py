class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in seen:
                ctr2 = i
                break
            else:
                seen[nums[i]] = i
        ctr1 = seen[to_find]
        return [ctr1, ctr2]
