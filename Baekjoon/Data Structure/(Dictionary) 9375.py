import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    clothes = dict()
    n = int(input())
    ans = 1
    for _ in range(n):
        name, kind = input().rstrip().split(" ")
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    for value in clothes.values():
        ans *= value + 1
    print(ans - 1)
