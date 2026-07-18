class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        res = 0
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        return res + min(prev, curr)