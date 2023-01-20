class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        answer = [[1 for _ in range(i + 1)] for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]

        return answer
