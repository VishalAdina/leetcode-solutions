class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = {}
        n = len(nums) // 2

        for num in nums:
            freq[num] = freq.get(num , 0) + 1

            if(freq[num] > n):
                return num


        
        