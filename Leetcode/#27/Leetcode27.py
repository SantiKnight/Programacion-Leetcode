class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cant_0 = nums.count(0)
        cant_1 = nums.count(1)
        n = len(nums)
        for i in range(0,cant_0):
            nums[i] = 0
        for i in range(cant_0,cant_0+cant_1):
            nums[i] = 1
        for i in range(cant_0+cant_1,n):
            nums[i] = 2
s = Solution()
s.sortColors([2,0,2,1,1,0])