class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = {}
        dic2 = {}
        for c in ransomNote: 
            if c not in dic1:
                dic1[c] = 1
            else:
                dic1[c] += 1
            dic2[c] = 0
        
        for c in magazine: 
            if c not in dic2:
                dic2[c] = 1
            else:
                dic2[c] += 1 

        for c in dic1:
            if dic1[c] > dic2[c]:
                return False
        return True