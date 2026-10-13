from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kl, kr = 1, max(piles)
        ans = kr
        while kl <= kr:
            km = (kl + kr) // 2
            time = 0
            for pile in piles:
                time += ceil(pile/km)
            if time > h:
                kl = km + 1
            else:
                ans = km
                kr = km - 1
        return ans
            

