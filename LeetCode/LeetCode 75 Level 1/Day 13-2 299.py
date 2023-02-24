from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A_cnt = 0
        for s, g in zip(secret, guess):
            if s == g:
                A_cnt += 1
        se = Counter(secret)
        gu = Counter(guess)
        B_cnt = 0
        for i in se:
            if i in gu:
                B_cnt += min(se[i], gu[i])

        return str(A_cnt) + 'A' + str(B_cnt - A_cnt) + 'B'
