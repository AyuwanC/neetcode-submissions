class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        n = len(nums)
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        buckets = [[] for _ in range(n+1)]
        for num, count in freq.items():
            buckets[count].append(num)
        ans = []
        for i in range(n, 0, -1):
            if buckets[i]:
                ans+=buckets[i]
        return ans[:k]
