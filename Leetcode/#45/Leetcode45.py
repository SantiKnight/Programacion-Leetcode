class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        time = customers[0][0]
        total = 0
        for c in customers:
            if time >= c[0]:
                time += c[1]
                total += time-c[0]
            else:
                time = c[0]+c[1]
                total += c[1]
            
        return total / len(customers)

s = Solution()
s.averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]])

# 2 -> 5    6 -> 9   7 -> 14   11 -> 17   15 -> 19    18 -> 20 
#    3         3        7         6           4           2