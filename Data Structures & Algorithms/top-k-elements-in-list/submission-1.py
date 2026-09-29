class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        return sorted(freq, key=lambda x: freq[x], reverse=True)[0:k]
