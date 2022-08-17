import sys
input = sys.stdin.readline

S = input().rstrip()
parts = []
length = len(S) + 1

for i in range(1, length):
    for j in range(0, length - i):
        parts.append(S[j:j+i])

print(len(set(parts)))
