class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i=0; i<s.length(); i++){
            String sub_str = "";
            int left = i;
            int right = i;
            while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
                sub_str = s.substring(left,right+1);
                if (sub_str.length() > res.length()){
                    res = sub_str;
                    
                }
                left -= 1;
                right += 1;
            }
            left = i;
            right = i+1;
            while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
                sub_str = s.substring(left,right+1);
                if (sub_str.length() > res.length()){
                    res = sub_str;
                }
                left -= 1;
                right += 1;
            }
        }
        return res;
    }
}