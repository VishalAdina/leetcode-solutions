class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        p_s = 0 
        count = 0 
        freq = {0:1}

        for num in nums:
            
            p_s += num

            count += freq.get(p_s - k , 0)
            freq[p_s] = freq.get(p_s , 0 ) +1

        return count


        