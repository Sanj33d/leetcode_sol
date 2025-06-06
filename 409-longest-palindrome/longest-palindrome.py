class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        ans = 0
        for x in s:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1

        for k in dic:
            if dic[k] > 1:
                if dic[k] % 2 == 0:
                    ans += dic[k]
                else:
                    ans += dic[k] - 1
        for k in dic:
            if dic[k] % 2 == 1:
                ans += 1
                return ans
        return ans