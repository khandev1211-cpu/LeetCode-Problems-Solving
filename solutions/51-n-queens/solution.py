class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, cols, diag1, diag2, path):
            if row == n:
                result.append(path)
                return
            for col in range(n):
                d1 = row - col
                d2 = row + col
                if col not in cols and d1 not in diag1 and d2 not in diag2:
                    backtrack(row + 1, cols | {col}, diag1 | {d1}, diag2 | {d2}, path + ["." * col + "Q" + "." * (n - col - 1)])
        
        result = []
        backtrack(0, set(), set(), set(), [])
        return result