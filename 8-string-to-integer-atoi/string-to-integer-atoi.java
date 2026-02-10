class Solution {
    public int myAtoi(String s) {
        String str2 = "";
        char signed = ' ';
        
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if ('0' <= c && c <= '9'){
                str2 += c;
            }
            else if(str2.length() == 0 && c == ' '){
                continue;
            }
            else if(str2.length() == 0 && (c == '+' || c =='-') ){
                str2 += c;
                signed = c;
            }
            else{
                break;
            }
        }
        
        double int_var = 0;
        if (str2.length() > 0) {
            if(str2.charAt(0) == '-' || str2.charAt(0) == '+'){
                str2 = str2.substring(1);
            }

            if(str2.length() == 0){
                int_var = 0;
            }
            else{
                if (signed == '-'){
                    int_var = 0 - Double.parseDouble(str2);
                }
                else{
                    int_var = Double.parseDouble(str2);
                }
            }
        }
        else{
            int_var = 0;
        }
        double int_min = -Math.pow(2, 31);
        double int_max = Math.pow(2, 31) - 1;

        if(int_var < int_min){
            return (int) int_min;
        }
        if(int_var > int_max){
            return (int) int_max;
        }
        return (int) int_var;

    }
}