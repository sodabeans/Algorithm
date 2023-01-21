class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        box = [[[] for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    curr = int(board[r][c])
                    if curr not in rows[r]:
                        rows[r].append(curr)
                    else:
                        return False
                    if curr not in cols[c]:
                        cols[c].append(curr)
                    else:
                        return False
                    if curr not in box[r // 3][c // 3]:
                        box[r // 3][c // 3].append(curr)
                    else:
                        return False

        return True
