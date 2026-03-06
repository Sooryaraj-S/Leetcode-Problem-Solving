class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range (0,len(nums)):
            for j in range (0,len(nums)-1-i):
                if (nums[j]>nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        