class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        p1 = edges[0][0]
        p2 = edges[0][1]
        for lista in edges:
            if p1 not in lista:
                p1 = 0
                break
            elif p2 not in lista:
                break
        if p1 != 0:
            return p1
        else:
            return p2
        
s = Solution()
s.findCenter([[1,2],[2,3],[4,2]])