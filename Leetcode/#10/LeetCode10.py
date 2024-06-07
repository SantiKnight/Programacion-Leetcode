class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        m = max(nums)
        n = len(nums)
        next()
        
        
        for i in range(n):
            if nums[i] == m:
                print(i)
                return i
        
s = Solution()
s.findPeakElement([3,3,2])