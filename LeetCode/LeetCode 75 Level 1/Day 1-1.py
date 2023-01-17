class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [nums[0]]
        for i in range(1, len(nums)):
            answer.append(nums[i] + answer[i - 1])
        return answer
