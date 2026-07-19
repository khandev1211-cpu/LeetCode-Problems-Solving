class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i + 1)
                comb.pop()
        backtrack(target, [], 0)
        return result