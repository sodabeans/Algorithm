import sys
input = sys.stdin.readline

answer = 0
N = int(input())
fear = list(map(int, input().split()))
fear.sort()
curr = 0

for i in range(len(fear)):
    curr += 1
    if fear[i] <= curr:
        answer += 1
        curr = 0

print(answer)
