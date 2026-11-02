class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack = []
        ctr = 0
        for i in nums:
            if i == 1:
                ctr += 1
            else:
                stack.append(ctr)
                ctr = 0
        stack.append(ctr)
        return max(stack)