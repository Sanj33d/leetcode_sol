class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        q = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and len(q) > 0:
            for rotten in range(len(q)):
                r, c = q.pop(0)
                for x, y in directions:
                    row = r + x
                    col = c + y

                    # checking in bound and fresh
                    if (0<=row<rows) and (0<=col<cols) and (grid[row][col]==1):
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else:
            return -1