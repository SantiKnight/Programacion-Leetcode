# class Solution:
#     def minIncrementForUnique(self, nums: list[int]) -> int:
        # MI SOLUCIÓN, ES DEMASIADO LENTA PARA EL PROBLEMA, RECURRI A CHAT GPT PARA QUE ME AYUDE A HACERLA MAS RAPIDA
        # t = 0
        # for n in nums:
        #     original = list(nums)
        #     if nums.count(n) != 1:
        #         while n in original:
        #             nums[nums.index(n)] += 1
        #             n = n+1
        #             t += 1
        # return t
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        t = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                t += prev + 1 - nums[i]
                prev += 1
            else:
                prev = nums[i]
        return t
    
s = Solution()
s.minIncrementForUnique([3,2,1,2,1,7])