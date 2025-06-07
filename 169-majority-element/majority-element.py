class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = {}
        for n in range(len(nums)):
            if nums[n] not in counter:
                counter[nums[n]] = 1
            else:
                counter[nums[n]] += 1

        counter2 = 0
        ans = None
        for n in counter:
            if counter[n] > counter2:
                counter2 = counter[n]
                ans = n
        return ans