class Solution:
    def myAtoi(self, s: str) -> int:
        str2 = ''
        signed = ""
        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                str2 += s[i]
            elif len(str2) == 0 and s[i] == " ":
                continue
            elif (len(str2) == 0) and (s[i] == "+" or s[i] == "-"):
                str2 += s[i]
                signed = s[i]
            else:
                break

        if len(str2) > 0:
            if str2[0] == "-":
                str2 = str2[1:]
            elif str2[0] == "+":
                str2 = str2[1:]
            if len(str2) == 0:
                int_var = 0
            else:
                if signed == "-":
                    int_var = 0 - int(str2)
                else:
                    int_var = int(str2)

        else:
            int_var = 0

        int_min = -2**31
        int_max = 2**31 - 1
        
        if int_var < int_min:
            return int_min
        if int_var > int_max:
            return int_max
        return int_var  
         
        