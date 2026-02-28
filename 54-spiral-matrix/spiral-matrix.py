class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ans = []

        r,c = 0,0
 
        boundary_right = len(matrix[0]) - 1
        boundary_bottom = len(matrix) - 1
        boundary_left = 0
        boundary_top = 0
      
        while boundary_top <= boundary_bottom and boundary_left <= boundary_right:
            #right
            for c in range(boundary_left, boundary_right + 1):
                ans.append(matrix[boundary_top][c])
            boundary_top += 1

            #down
            for r in range(boundary_top, boundary_bottom + 1):
                ans.append(matrix[r][boundary_right])
            boundary_right -= 1

            #left (only if still valid row range)
            if boundary_top <= boundary_bottom:
                for c in range(boundary_right, boundary_left - 1, -1):
                    ans.append(matrix[boundary_bottom][c])
                boundary_bottom -= 1

            #up (only if still valid col range)
            if boundary_left <= boundary_right:
                for r in range(boundary_bottom, boundary_top - 1, -1):
                    ans.append(matrix[r][boundary_left])
                boundary_left += 1

        return ans
        
        

        