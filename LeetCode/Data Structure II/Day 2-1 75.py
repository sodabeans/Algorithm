class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        white = 0
        red = 0
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            elif nums[white] == 1:
                white += 1
