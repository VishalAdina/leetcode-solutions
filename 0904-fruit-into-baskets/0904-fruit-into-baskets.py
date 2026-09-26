class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        right = 0 
        left = 0 
        freq = {}
        wmax = 0

        while(right < len(fruits)):

            if fruits[right] not in freq:
                freq[fruits[right]] = 0

            freq[fruits[right]] += 1


            while len(freq) > 2:

                freq[fruits[left]] -= 1

                if freq[fruits[left]]== 0:
                    del freq[fruits[left]]

                left += 1


            wmax = max(wmax , right - left + 1)
            right += 1

        return wmax 
            
                
