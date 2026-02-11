class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_dp = len(s) + 1
        dp = [False] * len_dp
        dp[0] = True
        trues = [0] 
        for i in range(1, len_dp):
            for j in trues:
                if s[j:i] in wordDict:
                    dp[i] = True
                    trues.append(i)
                    break
        return dp[-1]

        