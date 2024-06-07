class Solution:
    def numSteps(self, s: str) -> int:
        a = 0
        t = int(s, 2)
        while t != 1:
            a += 1
            if t % 2 == 0:
                t //= 2
            else:
                t += 1
        return a
s = Solution()
s.numSteps("1111")