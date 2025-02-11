class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxx = nums[0]
        summ = nums[0]

        for i in range(1, len(nums)):
            if summ < 0:
                summ = 0
            summ += nums[i]
            maxx = max(summ, maxx)
        return maxx
        
        
        # maxx = nums[0] # cc1: if first elem is max
        # for i in range(len(nums)):
            
        #     summ = nums[i]
        #     for j in range(i+1, len(nums)):
        #         summ += nums[j]
        #         maxx = max(summ, maxx) # cc 2: is subarr is max
            
        #     maxx = max(nums[i],maxx) # cc 3: if last elem is max

        # return maxx

    