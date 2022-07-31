import sys
input = sys.stdin.readline

S = input().rstrip()
zero = 0
one = 0
if S[0] == '0':
    zero += 1
else:
    one += 1

for idx in range(1, len(S)):
    if S[idx - 1] == S[idx]:
        continue
    else:
        if S[idx] == '0':
            zero += 1
        else:
            one += 1
print(min(zero, one))
