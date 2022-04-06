import sys

input = sys.stdin.readline

N = int(input())
pillars_input = list()
max_H = 0
max_L = 0

for _ in range(N):
    L, H = map(int, input().split())
    if H > max_H:
        max_H = H
        max_H_L = L
    if L > max_L:
        max_L = L
    pillars_input.append([L, H])

pillars = [0] * (max_L + 1)

for [l, h] in pillars_input:
    pillars[l] = h

for i in range(0, max_H_L):
    if pillars[i] > pillars[i + 1]:
        pillars[i + 1] = pillars[i]

for i in range(max_L, max_H_L, -1):
    if pillars[i] > pillars[i - 1]:
        pillars[i - 1] = pillars[i]

print(sum(pillars))
