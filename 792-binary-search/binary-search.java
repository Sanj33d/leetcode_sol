class Solution {
    public static int binsrch(int [] nums, int target, int left, int right){
        int mid = left + (right - left) / 2;
        // base case 1
        if (left > right){ 
            return -1;
        }
        // base case 2
        if (nums[mid] == target){
            return mid;
        }
        // recursive case 
        else {
            if (nums[mid] < target){
                return binsrch(nums, target, mid + 1, right);
            }
            else{
                return binsrch(nums, target, left, mid - 1);
            }
        }
    }

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        int ans = binsrch(nums, target, left, right);
        return ans;
    }
}