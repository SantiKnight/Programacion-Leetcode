class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        elementos = []
        for element in nums:
            if nums.count(element) == 1:
                elementos.append(element)
        return elementos
        
s = Solution()
s.singleNumber([1,1,0,-2147483648])