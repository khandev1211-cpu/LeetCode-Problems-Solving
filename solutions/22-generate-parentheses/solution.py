class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_p, close_p, current):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_p < n:
                backtrack(open_p + 1, close_p, current + '(')
            if close_p < open_p:
                backtrack(open_p, close_p + 1, current + ')')
        result = []
        backtrack(0, 0, '')
        return result