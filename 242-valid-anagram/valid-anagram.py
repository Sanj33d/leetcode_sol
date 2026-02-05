class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
        for j in range(len(t)):
            count[ord(t[j]) - ord("a")] -= 1
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True