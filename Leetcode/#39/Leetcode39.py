class Solution:
    def minDifference(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        min_diff = min(
            nums[n-1] - nums[3],
            nums[n-2] - nums[2],
            nums[n-3] - nums[1],
            nums[n-4] - nums[0]  
        )
        return min_diff
            
s = Solution()
s.minDifference([82,81,95,75,20])