class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        j = len(height) - 1
        res = 0
        i = 0

        while i<j:

            res = max(res,(j-i)*(min(height[i] , height[j])))

            if(height[i] < height[j]):
                i += 1 
            else:
                j -= 1

        return res