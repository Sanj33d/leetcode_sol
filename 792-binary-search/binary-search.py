class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        def binsrch(nums, left, right, target):
            mid = left + (right - left) // 2
            if left > right: # base case 1
                return -1

            if nums[mid] == target: # base case 2
                return mid
            else: # recursive  case
                if nums[mid] < target: # rc1
                    return binsrch(nums, mid + 1, right, target)
                else: # rc2
                    return binsrch(nums, left, mid - 1, target)
        ans = binsrch(nums, left, right, target)
        return ans
        