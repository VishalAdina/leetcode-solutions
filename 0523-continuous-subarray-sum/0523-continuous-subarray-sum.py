class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n= len(nums)
        prefix_sum = 0
        reminder_index = {0 : -1}

        for i in range(n):
            prefix_sum += nums[i]
            reminder = prefix_sum % k

            if reminder in reminder_index :
                if i - reminder_index[reminder] >=2:
                    return True

            else:
                reminder_index[reminder] = i
        return False

        