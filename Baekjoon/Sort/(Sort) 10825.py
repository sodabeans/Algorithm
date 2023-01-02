import sys
input = sys.stdin.readline

N = int(input())
info = []

for i in range(N):
    student = input().rstrip().split()
    info.append(student)

info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(N):
    print(info[i][0])
