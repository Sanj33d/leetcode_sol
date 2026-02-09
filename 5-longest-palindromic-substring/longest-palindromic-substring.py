class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_sub_str = ''
        for i in range(len(s)):
            # odd len
            sub_str = ''
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sub_str = s[left:right+1]
                if len(sub_str) > len(longest_sub_str):
                    longest_sub_str = sub_str

                left -= 1
                right += 1
            # even len
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sub_str = s[left:right+1]
                if len(sub_str) > len(longest_sub_str):
                    longest_sub_str = sub_str

                left -= 1
                right += 1
        return longest_sub_str



        