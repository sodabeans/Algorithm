import sys
input = sys.stdin.readline

N = int(input())
stairs = list()

for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[-1])
    sys.exit()

steps = [0]
steps.append(stairs[0])
steps.append(steps[1] + stairs[1]) # index error if N is 1

for i in range(3, N+1):
    # 3 steps before + 1 step before + curr OR 2 steps before + curr
    steps.append(max(stairs[i-2] + steps[i-3], steps[i-2]) + stairs[i-1])

print(steps[-1])
