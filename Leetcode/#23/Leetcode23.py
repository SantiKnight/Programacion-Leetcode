class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            suma = nums[i]
            for j in range(len(nums)):
                if i != j and j >= i-1:
                    suma += nums[j]
                    if suma%k == 0:
                        return True
        return False
s = Solution()
s.checkSubarraySum([5,0,0,0],3)

# Este fue mi codigo pero es demasido lento para Leetcode, asi que lo optimice utilizando ChatGPT:
# class Solution:
# def checkSubarraySum(self, nums: list[int], k: int) -> bool:
#     remainder_dict = {0: -1}
#     current_sum = 0
#     for i in range(len(nums)):
#         current_sum += nums[i]
#         remainder = current_sum % k
#         if remainder in remainder_dict:
#             if i - remainder_dict[remainder] > 1:
#                 return True
#         else:
#             remainder_dict[remainder] = i
#     return False