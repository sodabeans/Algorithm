class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        answer = False
        if len(nums) != len(set(nums)):
            answer = True

        return answer