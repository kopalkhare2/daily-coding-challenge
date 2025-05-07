class Solution:
    def isHappy(self, n: int) -> bool:
        unhappy_cycle = {4, 16, 37, 58, 89, 145, 42, 20}

        while n != 1:
            if n in unhappy_cycle:
                return False
            n = sum(int(digit) ** 2 for digit in str(n))
            
        return True
