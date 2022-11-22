# count sort
import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
count = [0] * (max(arr) + 1)

for idx in range(len(arr)):
    count[arr[idx]] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')
