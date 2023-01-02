import sys
input = sys.stdin.readline

N = int(input())
ans_list = list()

for i in range(666, N * 10000):
    if len(ans_list) == N:
        break
    if "666" in str(i):
        ans_list.append(i)

print(ans_list[-1])
