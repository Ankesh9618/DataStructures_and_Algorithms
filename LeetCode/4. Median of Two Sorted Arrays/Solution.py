class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = []
        num3 = nums1 + nums2
        num3.sort()
        if len(num3) % 2 == 0:
            return (num3[int(len(num3)/2)-1] + num3[int(len(num3)/2) ])/2
        else:
            return num3[int(len(num3)/2)]