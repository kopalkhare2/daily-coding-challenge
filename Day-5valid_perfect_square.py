class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return True  # 0 and 1 are perfect squares

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2  # Newton's iteration

        return x * x == num
