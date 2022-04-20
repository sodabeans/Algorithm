import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan_line = [int(input()) for _ in range(K)]

low = 1
high = max(lan_line)
ok_list = list()

while low <= high:
    target = 0
    mid = (low + high) // 2
    for line in lan_line:
        if line >= mid:
            target += line // mid
    if target >= N:
        ok_list.append(mid)
        low = mid + 1
    elif target < N:
        high = mid - 1

if ok_list:
    print(max(ok_list))
else:
    print(0)
