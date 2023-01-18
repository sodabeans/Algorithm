class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        check = {}
        answer = True
        for i in range(len(s)):
            # print(f'{s[i]} {t[i]}')
            if s[i] in check:
                if check[s[i]] == t[i]:
                    continue
                else:
                    answer = False
                    break
            else:
                if t[i] in check.values():
                    answer = False
                    break
                else:
                    check[s[i]] = t[i]
        return answer
