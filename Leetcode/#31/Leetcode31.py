class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        t = 0
        # for w in worker:
        #     m = 0
        #     for i in range(len(difficulty)):
        #         if w >= difficulty[i]:
        #             if profit[i] > m:
        #                 m = profit[i]
        #     t += m
        # return t
        # PRIMER SOLUCION, DEMASIADO LENTA
        # z = sorted(zip(profit, difficulty))
        # for w in worker:
        #     n = len(z)-1
        #     while n != -1:
        #         if w >= z[n][1]:
        #             t += z[n][0]
        #             break
        #         n -= 1
        # return t
        # SEGUNDA SOLUCION, MEJOR, PERO TODAVIA LENTA
        z = sorted(zip(difficulty, profit))
        worker.sort()

        max_profit_at_difficulty = [0] * len(z)
        max_profit_at_difficulty[0] = z[0][1]

        for i in range(1, len(z)):
            max_profit_at_difficulty[i] = max(max_profit_at_difficulty[i - 1], z[i][1])

        j = 0
        for w in worker:
            while j < len(z) and w >= z[j][0]:
                j += 1
            if j > 0:
                t += max_profit_at_difficulty[j - 1]

        return t
s = Solution()
s.maxProfitAssignment([13,37,58],[4,90,96],[34,73,45])