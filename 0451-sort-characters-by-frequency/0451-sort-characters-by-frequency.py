class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = {}

        for a in s:
            freq[a] = freq.get(a , 0) + 1


        res = ""
        for char in sorted(freq, key=freq.get, reverse=True):
            res += char * freq[char]


        return res





        