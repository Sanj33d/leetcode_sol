class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for i in range(len(s)):
            if 'A'<=s[i]<='Z':
                newstr += s[i].lower()
            elif 'a'<=s[i]<='z':
                newstr += s[i]
            elif '0'<=s[i]<='9':
                newstr += s[i]
        newstr2 = ''
        for j in range(len(newstr)-1,-1,-1):
            newstr2 += newstr[j]
        if newstr == newstr2:
            return True
        else:
            return False
            