class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        answer = []
        tmp = []
        for row in mat:
            for num in row:
                tmp.append(num)
                if len(tmp) == c:
                    answer.append(tmp)
                    tmp = []

        return answer
