import sys
input = sys.stdin.readline

K = int(input())
numbers = []

for _ in range(K):
    curr = int(input())
    if curr == 0:
        numbers.pop()
    else:
        numbers.append(curr)

print(sum(numbers))
