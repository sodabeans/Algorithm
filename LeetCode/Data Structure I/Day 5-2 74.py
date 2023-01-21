class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                for num in row:
                    if target == num:
                        return True
        return False
