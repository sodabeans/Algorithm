class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -1
        total_left = -nums[-1]
        total_right = sum(nums)
        for i in range(len(nums)):
            total_right -= nums[i]
            total_left += nums[i - 1]
            if total_left == total_right:
                answer = i
                break
        return answer
