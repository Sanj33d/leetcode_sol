class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # my approach: sliding window
        # new1: dict.get(key_i, 0) -> returns the value of key_i, but if key_i doesn't exist then returns 0
        # new2: dic.pop(key_i) -> removes both the key_i and val_i
        if len(p) > len(s):
            return []
        
        p_dic, s_dic = {}, {}
        for i in range(len(p)):
            p_dic[p[i]] = 1 + p_dic.get(p[i], 0)
            s_dic[s[i]] = 1 + s_dic.get(s[i], 0)
        if p_dic == s_dic:
            ans = [0]
        else:
            ans = []
        
        l = 0
        for r in range(len(p), len(s)):
            s_dic[s[r]] = 1 + s_dic.get(s[r], 0)
            s_dic[s[l]] -= 1 

            if s_dic[s[l]] == 0:
                s_dic.pop(s[l])
            l += 1
            if p_dic == s_dic:
                ans.append(l)
        return ans

