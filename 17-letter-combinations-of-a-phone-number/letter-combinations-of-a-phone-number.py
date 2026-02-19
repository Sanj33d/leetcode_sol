class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [""]
        
        mapper = {"2": 'abc',
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"}

        ans = [""]
        for i in range(len(digits)):
            chr_set = mapper[digits[i]]
            new_ans = []
            
            for letter in chr_set:
                for char in ans:
                    new_ans.append(char + letter)
            ans = new_ans
        return ans
                

        
        