class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # approach: bfs instead of dfs because initially there can be multiple rotten oranges which will rot fresh oranges at the same time
        ## since bfs, so using queue
        ### the loop will function till the moment when both fresh and rotten oranges exist
        time = 0 # ans
        fresh = 0 # num of fresh oranges
        rows = len(grid)
        cols = len(grid[0])
        
        q = []
        # appending rotten oranges in queue and counting the num of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # 4 directional tracker
        while fresh > 0 and len(q) > 0:
            for rotten in range(len(q)):
                r, c = q.pop(0) # pop(0) cuz it is q, so first one will be popped
                for x, y in directions:
                    row = r + x
                    col = c + y

                    # checking if (in bound) and (fresh)
                    if (0<=row<rows) and (0<=col<cols) and (grid[row][col]==1):
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        else:
            return -1