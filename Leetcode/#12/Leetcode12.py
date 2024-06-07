
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