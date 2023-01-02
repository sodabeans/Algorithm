import sys
input = sys.stdin.readline

N = int(input())
hall = []
teachers = []
for i in range(N):
    hall.append(list(input().rstrip().split()))
    for j in range(N):
        if hall[i][j] == 'T':
            teachers.append((i, j))


def search():
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r, c in teachers:
        for idx in range(4):
            new_r, new_c = r, c
            while 0 <= new_r < N and 0 <= new_c < N:
                if hall[new_r][new_c] == 'O':
                    break
                elif hall[new_r][new_c] == 'S':
                    return False
                new_r += directions[idx][0]
                new_c += directions[idx][1]
    return True


def selection(obstacle_cnt):
    if obstacle_cnt == 3:
        if search():
            print("YES")
            exit()
            return
    else:
        for i in range(N):
            for j in range(N):
                if hall[i][j] == 'X':
                    hall[i][j] = 'O'
                    selection(obstacle_cnt + 1)
                    hall[i][j] = 'X'


selection(0)
print("NO")
