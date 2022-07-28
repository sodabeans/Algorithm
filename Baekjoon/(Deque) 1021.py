from collections import deque
import copy
import sys
input = sys.stdin.readline


def from_start(queue, target):
    cnt = 0
    while queue[0] != target:
        tmp = queue.popleft()
        queue.append(tmp)
        cnt += 1
    return cnt, queue


def from_end(queue, target):
    cnt = 0
    while queue[0] != target:
        tmp = queue.pop()
        queue.appendleft(tmp)
        cnt += 1
    return cnt, queue


N, M = map(int, input().split())
out = list(map(int, input().split()))
queue = deque([i for i in range(1, N + 1)])
ans = 0

for idx in range(M):
    while True:
        if queue[0] == out[idx]:
            queue.popleft()
            break
        else:
            start = copy.deepcopy(queue)
            end = copy.deepcopy(queue)
            start_cnt, start_queue = from_start(start, out[idx])
            end_cnt, end_queue = from_end(end, out[idx])
            if start_cnt >= end_cnt:
                queue = end_queue
                ans += end_cnt
            else:
                queue = start_queue
                ans += start_cnt
print(ans)