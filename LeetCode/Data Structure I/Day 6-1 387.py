class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = len(s)
        for x in set(s):
            if s.count(x) == 1:
                answer = min(answer, s.index(x))
        if answer == len(s):
            answer = -1
        return answer
