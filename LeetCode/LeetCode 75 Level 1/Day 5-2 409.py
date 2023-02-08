class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = 0
        total = {}
        for c in s:
            if c in total:
                total[c] += 1
            else:
                total[c] = 1
        for c in total:
            if total[c] % 2 != 0:
                odd += 1
        if odd:
            return len(s) - odd + 1
        return len(s)
