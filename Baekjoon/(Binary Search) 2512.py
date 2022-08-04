import sys
input = sys.stdin.readline

N = int(input())
cities = list(map(int, input().split()))
M = int(input())
cities.sort()

if M >= sum(cities):
    print(cities[-1])
    exit()

low = 0
high = cities[-1]

while low <= high:
    mid = (low + high) // 2
    target = sum([min(c, mid) for c in cities])
    if target > M:
        high = mid - 1
    else:
        low = mid + 1

print(low - 1)
