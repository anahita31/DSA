class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Handle overflow edge case: -2^31 / -1 = 2^31 (exceeds INT_MAX)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Repeatedly subtract largest shifted multiples of divisor
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp result within 32-bit limits
        return max(INT_MIN, min(INT_MAX, quotient))