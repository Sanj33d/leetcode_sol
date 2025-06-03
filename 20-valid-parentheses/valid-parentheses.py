class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic1 = {'(' : 1, '{' : 2, '[' : 3}
        dic2 = {')' : 1, '}' : 2, ']' : 3}

        for i in range(len(s)):
            if s[i] in dic1:
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    popped = stack.pop()
                    if  dic1[popped] != dic2[s[i]]:
                        return False
                    else:
                        continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
