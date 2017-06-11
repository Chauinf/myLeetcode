class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        index = 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                nums[index] = nums[i]
                index += 1
            
        nums[index] = nums[-1]
        return index+1
    