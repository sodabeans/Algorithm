class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev_row = [1] * n
        curr_row = [0] * n
        for i in range(1, m):
            curr_row[0] = prev_row[0]
            for j in range(1, n):
                curr_row[j] = prev_row[j] + curr_row[j - 1]
            prev_row = curr_row
            curr_row = [0] * n
        return prev_row[-1]
