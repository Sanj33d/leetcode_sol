class Solution {
    public boolean isAnagram(String s, String t) {
        int count[] = new int[26];
        for(int i=0; i<s.length(); i++){
            count[s.charAt(i)-'a'] += 1;
        }
        for(int j=0; j<t.length(); j++){
            count[t.charAt(j) - 'a'] -= 1;
        }
        for(int k=0; k<count.length; k++){
            if (count[k] != 0){
                return false;
            }
        }
        return true;
    }
}