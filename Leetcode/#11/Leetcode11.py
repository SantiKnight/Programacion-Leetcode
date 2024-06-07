class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximo = 0
        ventana = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                ventana += 1
            else:
                ventana = 0
            
            if maximo < ventana:
                maximo = ventana
                
        return maximo
        
s = Solution()
s.findMaxConsecutiveOnes([1,1,0,1,1,1])