class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n):
            target = -nums[i]
            total = set()
            for j in range(i+1, n):
                complement = target - nums[j]
                if complement not in total:
                    total.add(nums[j])
                else:
                    anselement = tuple(sorted([-target, nums[j], complement]))
                    if anselement not in ans:
                        ans.add(anselement)
        

        return [list(x) for x in ans]