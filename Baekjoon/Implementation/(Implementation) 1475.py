import math
import sys
input = sys.stdin.readline

room_num = list(input().rstrip())
cnt = [0 for _ in range(10)]

for num in room_num:
    cnt[int(num)] += 1

difference = math.floor(abs(cnt[6] - cnt[9]) / 2)
if cnt[6] > cnt[9]:
    cnt[6] = cnt[6] - difference
    cnt[9] = cnt[9] + difference
elif cnt[6] < cnt[9]:
    cnt[6] = cnt[6] + difference
    cnt[9] = cnt[9] - difference

print(max(cnt))
