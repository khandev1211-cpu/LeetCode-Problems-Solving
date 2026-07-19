class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        # Handle special case of overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while (temp << 1) <= dividend:
                temp <<= 1
                i <<= 1
            dividend -= temp
            quotient += i
        return sign * quotient