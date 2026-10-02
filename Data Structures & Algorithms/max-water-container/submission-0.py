class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        area = 0
        while i!=j:
            h1, h2 = heights[i], heights[j]
            area = max(area, (j-i)*min(h1, h2))
            if h1 < h2:
                i+=1
            else:
                j-=1
        return area