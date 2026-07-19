class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_p, close_p, path):
            if len(path) == 2 * n:
                result.append(path)
                return
            if open_p < n:
                backtrack(open_p + 1, close_p, path + '(')
            if close_p < open_p:
                backtrack(open_p, close_p + 1, path + ')')
        result = []
        backtrack(0, 0, '')
        return result