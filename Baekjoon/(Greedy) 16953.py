import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1

while B != A:
    curr = B
    if B % 10 == 1:  # if removing 1 is available
        B = B // 10
        cnt += 1
    elif B % 2 == 0:  # if divisible by 2
        B = B // 2
        cnt += 1
    if curr == B:  # if no change
        print("-1")
        exit()

print(cnt)
