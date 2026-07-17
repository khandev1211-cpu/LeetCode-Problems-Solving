from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxVal = max(nums)
        
        # cnt[v] = how many elements equal v
        cnt = [0] * (maxVal + 1)
        for x in nums:
            cnt[x] += 1
        
        # freq[v] = how many elements are multiples of v
        freq = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            for multiple in range(v, maxVal + 1, v):
                freq[v] += cnt[multiple]
        
        # pairs[v] = pairs where both elements are multiples of v
        exactGCD = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            f = freq[v]
            exactGCD[v] = f * (f - 1) // 2
        
        # subtract overcounted pairs to get EXACT gcd counts (high -> low)
        for v in range(maxVal, 0, -1):
            for multiple in range(2 * v, maxVal + 1, v):
                exactGCD[v] -= exactGCD[multiple]
        
        # prefix[v] = number of pairs with gcd <= v
        prefix = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            prefix[v] = prefix[v - 1] + exactGCD[v]
        
        # answer each query via binary search on the prefix array
        answer = []
        for q in queries:
            v = bisect.bisect_right(prefix, q)
            answer.append(v)
        
        return answer


# ---- quick test against the given examples ----
if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdValues([2,3,4], [0,2,2]))        # [1, 2, 2]
    print(sol.gcdValues([4,4,2,1], [5,3,1,0]))    # [4, 2, 1, 1]
    print(sol.gcdValues([2,2], [0,0]))            # [2, 2]
