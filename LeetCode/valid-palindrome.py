class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """91 ms, 16.1 MB"""
        s_list = []
        for c in s:
            if c.isalnum():
                s_list.append(c.lower())
        print(s_list)

        s_length = len(s_list)

        for i in range(s_length // 2):
            if s_list[i] != s_list[s_length - 1 - i]:
                return False

        return True
