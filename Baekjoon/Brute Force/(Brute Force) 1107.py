import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
button = list(map(str, input().rstrip().split()))
ans = abs(N - 100)  # difference from current channel = maximum count

if M == 0:  # no broken buttons
    if N == 100:
        print(0)
    else:
        ans = min(ans, len(str(N)))
        print(ans)
    exit()

for num in range(1000001):
    flag = True
    num = str(num)
    for idx in range(len(num)):  # check each digit of current number option
        if num[idx] in button:  # not applicable if there is a broken button
            flag = False
            break
    if flag:
        ans = min(ans, len(num) + abs(int(num) - N))  # current number + move up or down
print(ans)
