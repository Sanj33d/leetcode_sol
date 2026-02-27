class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = []
        for i in range(m):
            ans.append([0]*n)
        ans[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    ans[i][j] = ans[i][j-1]
                elif j == 0:
                    ans[i][j] = ans[i-1][j]
                else:
                    ans[i][j] = ans[i][j-1] + ans[i-1][j]
        return ans[-1][-1]
                
        