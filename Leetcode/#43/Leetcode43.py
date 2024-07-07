import math
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        vacias = 0
        total += numBottles
        vacias = numBottles
        while vacias >= numExchange:
            numBottles = math.floor(vacias / numExchange)
            vacias = ((vacias/numExchange) - math.floor(vacias / numExchange))*numExchange
            total += numBottles
            vacias += numBottles
        return total
    
s = Solution()
s.numWaterBottles(15,4)