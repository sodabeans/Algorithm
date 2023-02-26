class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr_str = ''
        curr_cnt = ''
        stack = []
        for c in s:
            if c == '[':
                stack.append((curr_str, int(curr_cnt)))
                curr_str = ''
                curr_cnt = ''
            elif c == ']':
                ans_str, ans_cnt = stack.pop()
                curr_str = ans_str + ans_cnt * curr_str
            else:
                if c.isdigit():
                    curr_cnt += c
                else:
                    curr_str += c
        return curr_str
