class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int len_dp = s.length() + 1;
        boolean dp [] = new boolean[len_dp];
        dp[0] = true;

        List<Integer> trues = new ArrayList<>();
        trues.add(0);

        for(int i=1; i<len_dp; i++){
            for (int j : trues){
               if(wordDict.contains(s.substring(j,i))){
                dp[i] = true;
                trues.add(i);
                break;
               } 
            }
        }
        return dp[len_dp - 1];
    }
}