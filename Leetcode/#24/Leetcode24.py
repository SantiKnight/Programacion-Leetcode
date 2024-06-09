class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # total = 0
        # for i in range(len(nums)):
        #     suma = nums[i]
        #     if suma%k == 0:
        #         total += 1
        #     for j in nums[i+1:]:
        #         suma += j
        #         if suma%k == 0:
        #             total += 1
        # return total
        
        # Diccionario para almacenar la frecuencia de restos
        remainder_count = {0: 1}
        current_sum = 0
        total = 0
        
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            
            # Asegurar que el resto sea positivo
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                total += remainder_count[remainder]
            
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return total
s = Solution()
s.subarraysDivByK([4,5,0,-2,-3,1],5)