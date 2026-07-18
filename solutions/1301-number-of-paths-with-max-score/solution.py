from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        grid = [list(row) for row in board]

        # dp[i][j] = (max_sum, count) or (-1, 0) if unreachable
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)  # start at 'S'

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                if grid[i][j] == 'X':
                    continue

                best_sum = -1
                best_cnt = 0

                for di, dj in ((1, 0), (0, 1), (1, 1)):
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n:
                        s, c = dp[ni][nj]
                        if s < 0:
                            continue
                        if s > best_sum:
                            best_sum = s
                            best_cnt = c
                        elif s == best_sum:
                            best_cnt = (best_cnt + c) % MOD

                if best_sum < 0:
                    continue  # no way to reach this cell

                val = 0 if grid[i][j] == 'E' else int(grid[i][j])
                dp[i][j] = (best_sum + val, best_cnt)

        max_sum, count = dp[0][0]
        if max_sum < 0:
            return [0, 0]
        return [max_sum, count % MOD]