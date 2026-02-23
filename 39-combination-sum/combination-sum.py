class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def rec_func(remaining, start, lis):
            # bc
            if remaining == 0:
                ans.append(lis[:])
                return
            if remaining < 0:
                return 
            else:
                # rec case
                for i in range(start, len(candidates)):
                    c = candidates[i]
                    if c > remaining:
                        break
                    lis.append(c)
                    rec_func(remaining - c, i, lis)
                    lis.pop()
        rec_func(target, 0, [])
        return ans
                

        