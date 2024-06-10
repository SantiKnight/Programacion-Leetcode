
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        aux = sorted(heights)
        total = 0
        for i in range(len(aux)):
            if aux[i] != heights[i]:
                total += 1
        return total
    
s = Solution()
s.heightChecker([1,1,4,2,1,3])