class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        answer = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            curr = min(curr, prices[i])
            answer = max(answer, prices[i] - curr)

        return answer
