class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        nums=sorted(nums)
        if len(nums)%2!=0:
            mid=len(nums)/2
            mid=int(mid)
            m=nums[mid]
            return m
        else:
            mid=len(nums)/2
            mid=int(mid)
            m=(nums[mid]+nums[mid-1])/2.0
            return m