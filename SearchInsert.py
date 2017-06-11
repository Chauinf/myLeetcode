class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        for i, value in enumerate(nums):
            if value > target:
                    return i
        

#key:nums.index