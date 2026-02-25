class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = 0
        for elem in nums:
            summ += elem
        if summ % 2 == 1:
            return False
        else:
            dp = set()
            dp.add(0)
            for num in nums:
                dp_2 = set()
                for d in dp:
                    dp_2.add(d + num)
                    dp_2.add(d)
                dp = dp_2
        if (summ / 2) in dp:
            return True
        else:
            return False
   
