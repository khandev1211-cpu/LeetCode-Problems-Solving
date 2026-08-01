class Solution:
    def grayCode(self, n: int) -> List[int]:
        def generate_gray_code(n):
            if n == 1:
                return [0, 1]
            else:
                prev_gray_code = generate_gray_code(n - 1)
                curr_gray_code = []
                for code in prev_gray_code:
                    curr_gray_code.append(code)
                for code in reversed(prev_gray_code):
                    curr_gray_code.append(code + (1 << (n - 1)))
                return curr_gray_code
        return generate_gray_code(n)