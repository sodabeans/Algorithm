import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
board = [[ord(x) - 65 for x in _] for _ in board]

visited = [0 for _ in range(26)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for idx in range(4):
        dx, dy = directions[idx]
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < R and 0 <= new_y < C and not visited[board[new_x][new_y]]:
            visited[board[new_x][new_y]] = 1
            search(new_x, new_y, cnt + 1)
            visited[board[new_x][new_y]] = 0


answer = 1
visited[board[0][0]] = 1
search(0, 0, answer)
print(answer)
