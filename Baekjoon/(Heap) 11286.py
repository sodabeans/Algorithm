import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap_neg = []
heap_pos = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(heap_neg) == 0 and len(heap_pos) == 0:
            print("0")
        else:
            if len(heap_neg) == 0:
                print(heapq.heappop(heap_pos))
                continue
            if len(heap_pos) == 0:
                print(-(heapq.heappop(heap_neg)))
                continue
            if heap_neg[0] <= heap_pos[0]:
                print(-(heapq.heappop(heap_neg)))
            else:
                print(heapq.heappop(heap_pos))
    elif num < 0:  # negative number
        heapq.heappush(heap_neg, -num)
    else:  # positive number
        heapq.heappush(heap_pos, num)
