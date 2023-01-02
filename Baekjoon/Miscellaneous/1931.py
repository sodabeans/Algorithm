import sys
input = sys.stdin.readline

N = int(input())
time = list()

for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))

# first, sort by starting time
time.sort()
# then, sort by ending time
time.sort(key = lambda x: x[1]) # https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/

_, prev_end = time[0]
cnt = 1

for i in range(1, len(time)):
    start, end = time[i]
    if start < prev_end:
        continue
    prev_end = end
    cnt += 1

print(cnt)