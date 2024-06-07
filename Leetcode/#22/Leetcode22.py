class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2:list[int]) -> float:
        nums1.extend(nums2)
        l = len(nums1)
        nums1 = sorted(nums1)
        if l % 2 == 0:
            return (nums1[int(l/2)-1] + nums1[int(l/2)]) /2
        else:
            return nums1[int(l/2)]