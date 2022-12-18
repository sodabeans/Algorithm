import sys
input = sys.stdin.readline

S = input().rstrip()
answer = int(S[0])

for i in range(1, len(S)):
    curr = int(S[i])
    if answer + curr >= answer * curr:
        answer += curr
    else:
        answer *= curr
print(answer)
