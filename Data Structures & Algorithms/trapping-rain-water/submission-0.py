class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        leftmax = rightmax = 0
        area = 0
        while i <= j:
            if leftmax <= rightmax:
                leftmax = max(leftmax, height[i])
                area += leftmax - height[i]
                i+=1
            else:
                rightmax = max(rightmax, height[j])
                area += rightmax - height[j]
                j-=1
        return area
