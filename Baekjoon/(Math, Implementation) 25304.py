import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
total = 0
for _ in range(N):
    p, q = map(int, input().split())
    total += p * q

if total == X:
    print("Yes")
else:
    print("No")
