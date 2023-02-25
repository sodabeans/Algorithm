class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_result = ''
        for c in s:
            if c == '#':
                s_result = s_result[:-1]
            else:
                s_result += c
        t_result = ''
        for c in t:
            if c == '#':
                t_result = t_result[:-1]
            else:
                t_result += c
        return s_result == t_result
