class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [0] * (rowIndex + 1)
        dp[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                dp[j] = dp[j] + dp[j - 1]
        return dp
