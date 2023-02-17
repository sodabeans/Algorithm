class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 2], cost[i - 1])
        return min(cost[-1], cost[-2])
