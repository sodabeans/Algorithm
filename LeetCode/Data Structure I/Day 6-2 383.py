class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for x in set(ransomNote):
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True
