import sys
input = sys.stdin.readline

N = int(input())
hall = list(list(input().rstrip().split()) for _ in range(N))
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
students = []
teachers = []
obstacles = 3

for i in range(N):
    for j in range(N):
        if hall[i][j] == 'S':
            students.append((i, j))
        elif hall[i][j] == 'T':
            teachers.append((i, j))

if not students or not teachers:
    print("YES")
    exit()

for x_t, y_t in teachers:
    for idx in range(4):
        for j in range(1, N):
            new_x = x_t + (directions[idx][0] * j)
            new_y = y_t + (directions[idx][1] * j)
            if 0 <= new_x < N and 0 <= new_y < N:
                if hall[new_x][new_y] == 'T' or hall[new_x][new_y] == 'O':
                    break
                elif hall[new_x][new_y] == 'S':
                    if obstacles:
                        obstacles -= 1
                        hall[x_t + directions[idx][0]][y_t + directions[idx][1]] = 'O'
                    else:
                        print("NO")
                        exit()

print("YES")
