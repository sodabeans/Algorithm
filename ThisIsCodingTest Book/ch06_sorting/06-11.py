import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
arr.sort(key=lambda item: item[1])
for i in range(len(arr)):
    print(arr[i][0], end=' ')
