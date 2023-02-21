class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_len = len(p)
        s_len = len(s)
        answer = []
        if p_len > s_len:
            return answer

        cnt = {}
        for c in p:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1

        for i in range(p_len - 1):
            if s[i] in cnt:
                cnt[s[i]] -= 1

        for i in range(-1, s_len - p_len + 1):
            flag = True
            if i != -1 and s[i] in cnt:
                cnt[s[i]] += 1
            end = i + p_len
            if end < s_len and s[end] in cnt:
                cnt[s[end]] -= 1
            for _ in cnt.values():
                if _ != 0:
                    flag = False
                    break
            if flag:
                answer.append(i + 1)

        return answer
