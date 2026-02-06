class Solution {
    public boolean isPalindrome(String s) {
        String new_str = "";
        for (int i=0; i<s.length(); i++){
            if(Character.isLetterOrDigit(s.charAt(i))){
                new_str += Character.toLowerCase(s.charAt(i));
            }
        }
        int left = 0;
        int right = new_str.length() - 1;
        while (left<right){
            if (new_str.charAt(left) != new_str.charAt(right)){
                return false;
            }
            left ++;
            right --;
        }
        return true;
         
    }
}