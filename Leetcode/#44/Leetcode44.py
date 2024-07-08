class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = []
        arranca = 0
        for i in range(1, n+1):
            l.append(i)
        while len(l) != 1:
            recorre = k
            while recorre != 0:
                for i in range(len(l)):
                    i = arranca+i
                    if i >= len(l):
                        arranca = 0
                        break
                    recorre -= 1
                    if recorre == 0:
                        l.pop(i)
                        arranca = i
                        break
        return l[0]

s = Solution()
s.findTheWinner(6,5)