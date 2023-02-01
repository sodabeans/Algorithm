class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        answer = True
        idx = 0
        for i in range(len(s)):
            flag = False
            for j in range(idx, len(t)):
                if s[i] == t[j]:
                    idx = j + 1
                    flag = True
                    break
            answer = flag
            if flag == False:
                break

        return answer
