class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = {}
        for num in nums:
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        answer = sorted(check.items(), reverse=True, key=lambda item: item[1])
        return answer[0][0]
