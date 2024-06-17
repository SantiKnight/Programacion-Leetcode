from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)
            if b == int(b):
                return True
        return False
    
s = Solution()
s.judgeSquareSum(2)