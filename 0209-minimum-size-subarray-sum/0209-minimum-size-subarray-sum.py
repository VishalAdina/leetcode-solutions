class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        wmin = float('inf')
        
        left = 0 
        right = 0
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                wmin = min(wmin , right-left +1)
                
                sum -= nums[left]
                left += 1

        if wmin == float('inf'):
            return 0 

        return wmin
            

            

             
        