class Solution:
    def maxArea(self, height: List[int]) -> int:
        # approach1: two pointer theory (left most end, right most end)
        ## new: Python doesn't go to the next iteration after executing any of the incremental var (like l) or decremental var (like r). Instead of it, python reads all the codes of the loop block before going to the next iteration.
        l_idx = 0 
        r_idx = len(height) - 1 
        max_area = 0

        while l_idx < r_idx:
            left = height[l_idx]
            right = height[r_idx]

            area = (r_idx - l_idx) * min(left, right)
            max_area = max(max_area, area)
            if left < right:
                l_idx += 1
            else: 
                r_idx -= 1
        return max_area
