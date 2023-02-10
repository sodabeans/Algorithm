class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                answer = mid
                break
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return answer
