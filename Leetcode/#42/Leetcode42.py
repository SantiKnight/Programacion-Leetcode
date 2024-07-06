class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        incr = 1
        while time != 0:
            i += incr
            time -= 1
            if i == n:
                incr = -1
            if i == 1:
                incr = 1
        return i