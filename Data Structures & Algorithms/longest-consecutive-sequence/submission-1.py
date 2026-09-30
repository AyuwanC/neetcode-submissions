class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        starts = set()
        for i in nums:
            if i-1 in numset:
                pass
            else:
                starts.add(i)
        ctr = set([0])
        for i in starts:
            j = 1
            while j < len(nums):
                if i+j in numset:
                    j+=1
                else:
                    break
            ctr.add(j)
        return max(ctr)
