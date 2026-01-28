class Solution(object):
    def maxSubArray(self, nums):
        res = nums[0]
        total = 0
        for i in nums:
            if total<0:
                total = 0
            total += i
            res = max(res,total)
        return res
