class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = []
        for num in nums:
            if num in check:
                check.remove(num)
            else:
                check.append(num)
        return check[0]
