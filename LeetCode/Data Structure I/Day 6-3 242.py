class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = [x for x in t]
        for x in s:
            if x in t:
                t.remove(x)
            else:
                return False
        if len(t) == 0:
            return True
        else:
            return False
