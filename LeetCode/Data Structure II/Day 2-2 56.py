class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        intervals.sort(key=lambda i:i[0])
        for start, end in intervals:
            if answer and start <= answer[-1][1]:
                answer[-1][1] = max(end, answer[-1][1])
            else:
                answer.append([start, end])

        return answer
