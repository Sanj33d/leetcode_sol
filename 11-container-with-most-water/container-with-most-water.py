class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            left = height[l]
            right = height[r]

            area = (r-l) * min(left, right)
            max_area = max(max_area, area)
            if left < right:
                l += 1
            else: 
                r -= 1
        return max_area
