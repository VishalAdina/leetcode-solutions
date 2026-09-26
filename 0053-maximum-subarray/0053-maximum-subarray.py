class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        max_sum = nums[0]
        for i in range(1 ,len(nums)):
            sum += nums[i]

            if(nums[i] > sum):
                sum = nums[i]

            max_sum = max(max_sum , sum)

        return max_sum

            

        