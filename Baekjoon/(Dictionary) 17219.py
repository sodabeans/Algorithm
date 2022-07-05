import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = dict()

for _ in range(N):
    address, password = input().rstrip().split(" ")
    memo[address] = password

for _ in range(M):
    target = input().rstrip()
    print(memo[target])
