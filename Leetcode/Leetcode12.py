# You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, 
# both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] 
# units to run. You are also given an integer budget.

# The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), 
# where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is 
# the sum of running costs among the k robots.

# Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.

# Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
# Output: 3
# Explanation: 
# It is possible to run all individual and consecutive pairs of robots within budget.
# To obtain answer 3, consider the first 3 robots. 
# The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
# It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.
from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        left = 0
        ans = 0
        current_sum = 0
        max_charge = deque()
        
        for right in range(len(chargeTimes)):
            # Actualizar la ventana de runningCosts y max_charge
            current_sum += runningCosts[right]
            while max_charge and max_charge[-1] < chargeTimes[right]:
                max_charge.pop()
            max_charge.append(chargeTimes[right])
            
            # Calcular el costo actual de la ventana
            k = right - left + 1
            current_cost = max_charge[0] + k * current_sum
            
            # Ajustar la ventana izquierda si el costo excede el presupuesto
            while current_cost > budget:
                if max_charge[0] == chargeTimes[left]:
                    max_charge.popleft()
                current_sum -= runningCosts[left]
                left += 1
                k = right - left + 1
                if k > 0:
                    current_cost = max_charge[0] + k * current_sum
                else:
                    current_cost = 0
            
            # Actualizar la respuesta
            ans = max(ans, right - left + 1)
        
        return ans
s = Solution()
s.maximumRobots([8,76,74,9,75,71,71,42,15,58,88,38,56,59,10,11], [1,92,41,63,22,37,37,8,68,97,39,59,45,50,29,37], 412)