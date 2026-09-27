class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        max_prd = nums[0]
        min_prd = nums[0]

        for i in range(1,len(nums)):

            new_min = min(nums[i], nums[i]*min_prd ,nums[i]*max_prd)
            new_max = max(nums[i] , nums[i]*min_prd,nums[i]*max_prd)

            max_prd = new_max
            min_prd = new_min


            ans = max(ans , max_prd)
        return ans

        