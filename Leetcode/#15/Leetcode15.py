class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        item = []
        for i in range(len(nums)):
            if nums[i] > 0:
                item = nums[i:]
                break
        if len(item) > 0:
            for i in range(len(item)):
                if item[i] != i+1:
                    return i+1
                else:
                    if i+1 == len(item):
                        return i+2
        else:
            return 1
        
        
            
            
s = Solution()
s.firstMissingPositive([0,1,3,1])