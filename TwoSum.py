class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = False
        amount = len(nums)
        result = []
        for i, value in enumerate(nums):
            for j in range(1,amount-i):
                if value + nums[-j] == target:
                    result.append(i)
                    result.append(amount-j)
                    flag = True
                    break
        
            if flag is True:
                break
    
        return result  