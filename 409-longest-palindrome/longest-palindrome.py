class Solution:
    def longestPalindrome(self, s: str) -> int:
        even_count = 0
        odd_count = 0
        counter = {}

        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1

        for key in counter:
            if counter[key] % 2 == 0:
                if counter[key] >= 2:
                    even_count += counter[key]
            else:
                if counter[key] > 1:
                    even_count += counter[key] - 1
                odd_count = 1
        return odd_count + even_count
                    
