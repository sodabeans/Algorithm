import sys
input = sys.stdin.readline

N = list(input().rstrip())
total = 0
for i in range(len(N)):
    if i < len(N) // 2:
        total += int(N[i])
    else:
        total -= int(N[i])

if total == 0:
    print("LUCKY")
else:
    print("READY")
