import heapq

def check_neighbor(classroom, like_students, x, y, check_like_only=False):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    empty = 0
    like = 0
    for dx, dy in directions:
        if 0 <= x + dx < N and 0 <= y + dy < N:
            if classroom[x + dx][y + dy] in like_students:
                like += 1
            if not check_like_only and classroom[x + dx][y + dy] == 0:
                empty += 1
    return empty, like


N = int(input())
answer = 0
visited = [0 for _ in range((N ** 2) + 1)]
classroom = [[0] * N for _ in range(N)]
students = {}
for _ in range(N ** 2):
    curr_student, s1, s2, s3, s4 = map(int, input().split())
    students[curr_student] = [s1, s2, s3, s4]

for curr_student in students.keys():
    options = []
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                empty, like = check_neighbor(classroom, students[curr_student], i, j)
                heapq.heappush(options, (-like, -empty, i, j))
    _, _, x, y = heapq.heappop(options)
    classroom[x][y] = curr_student

score_table = [0, 1, 10, 100, 1000]

for i in range(N):
    for j in range(N):
        _, like_score = check_neighbor(classroom, students[classroom[i][j]], i, j, check_like_only=True)
        answer += score_table[like_score]

print(answer)
