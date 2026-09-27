class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = 0
        global_max = nums[0]
        curr_min = 0
        global_min = nums[0]
        total = 0

        for i in range(len(nums)):

            curr_max = max(curr_max+nums[i] , nums[i])
            curr_min = min(curr_min+nums[i] , nums[i])

            total += nums[i]

            global_max = max(global_max,curr_max)
            global_min = min(global_min , curr_min)

        if(global_max < 0):
            return global_max


        return max(global_max , total-global_min) 


            

        

                

        