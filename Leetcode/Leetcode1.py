class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    result = [i,j]
                    return result

s = Solution()
s.twoSum([11,2,3,4], 6)