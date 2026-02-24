class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # bc
        if len(nums) == 1:
            return [nums.copy()]
        # rc
        for i in range(len(nums)):
            popped = nums.pop(0)
            permutations = self.permute(nums)
            for perm in permutations:
                perm.append(popped)
            ans.extend(permutations)
            nums.append(popped)
        return ans

        