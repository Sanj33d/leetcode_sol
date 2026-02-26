class Solution {
    public boolean canPartition(int[] nums) {
        int summ = 0;
        for (int num : nums){
            summ += num;
        }
        if (summ % 2 != 0){
            return false;
        }
        Set<Integer> dp = new HashSet<>();
        dp.add(0);
        for (int num : nums){
            Set<Integer> dp_new = new HashSet<>();
            for (int d : dp){
                dp_new.add(d);
                dp_new.add(d + num);
            }
            dp = dp_new;
        }
        if (dp.contains(summ/2)){
            return true;
        }
        else{
            return false;
        }
    }
}