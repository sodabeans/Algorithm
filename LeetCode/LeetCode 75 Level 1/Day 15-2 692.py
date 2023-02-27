class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_cnt = collections.Counter(words)
        word_cnt = sorted(word_cnt.items(), key = lambda x: (-x[1], x[0]), reverse=True)
        answer = []
        for i in range(len(word_cnt) - 1 , len(word_cnt) - k - 1, -1):
            answer.append(word_cnt[i][0])
        return answer
