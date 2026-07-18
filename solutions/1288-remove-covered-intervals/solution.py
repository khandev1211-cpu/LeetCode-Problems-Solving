class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        right = -1
        for _, r in intervals:
            if r > right:
                count += 1
                right = r
        return count