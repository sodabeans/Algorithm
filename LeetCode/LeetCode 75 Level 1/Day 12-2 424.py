class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        answer = 0
        cnt = 0
        check = {}
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = 1
            else:
                check[s[i]] += 1
            cnt = max(cnt, check[s[i]])
            if answer - cnt >= k:
                check[s[i - answer]] -= 1
            else:
                answer += 1
        return answer
