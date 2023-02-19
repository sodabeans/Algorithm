class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        initial_color = image[sr][sc]
        if initial_color == color:
            return image

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return
            if image[r][c] != initial_color:
                return
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)

        return image
