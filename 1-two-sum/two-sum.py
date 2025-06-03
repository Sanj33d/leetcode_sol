class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    ans.append(idx1)
                    ans.append(idx2)
                    return ans
        
        