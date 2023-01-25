class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                check.append(c)
            else:
                if len(check) == 0:
                    return False
                if c == ')' and check[-1] == '(':
                    check.pop()
                elif c == ']' and check[-1] == '[':
                    check.pop()
                elif c == '}' and check[-1] == '{':
                    check.pop()
                else:
                    return False
        if len(check) != 0:
            return False
        return True
