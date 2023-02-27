import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for s in stones:
            heapq.heappush(heap, (-s, s))

        while len(heap) > 1:
            y = heapq.heappop(heap)[1]
            x = heapq.heappop(heap)[1]
            curr = y - x
            if curr:
                heapq.heappush(heap, (-curr, curr))
        if len(heap):
            return heap[0][1]
        else:
            return 0
