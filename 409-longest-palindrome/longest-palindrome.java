import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestPalindrome(String s) {
        int even_count = 0;
        int odd_count = 0;

        Map<Character, Integer> counter = new HashMap<>();
        for (int i=0; i<s.length(); i++){
            char key = s.charAt(i);
            if(!counter.containsKey(key)){
                counter.put(key, 1);
            }
            else{
                counter.put(key, counter.get(key) + 1);
            }
        }

        for (char key : counter.keySet()){
            int count = counter.get(key);
            if (count % 2 == 0){
                if (count >= 2){
                    even_count += count;
                }
            }
            else{
                if (count > 1){
                    even_count += count - 1;
                }
                odd_count = 1;
            }
        }
        return even_count + odd_count;
    }
}