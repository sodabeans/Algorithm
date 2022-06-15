import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    heap_max = []
    heap_min = []
    k = int(input())
    visited = [False] * k

    for idx in range(k):
        calc, n = map(str, input().split())
        n = int(n)
        if calc == 'I':  # insert
            # group input and index together
            heapq.heappush(heap_max, [-n, idx])
            heapq.heappush(heap_min, [n, idx])
            visited[idx] = True
        else:  # delete
            if n == 1:  # delete max
                while heap_max and not visited[heap_max[0][1]]:
                    # element exists and element was not visited
                    heapq.heappop(heap_max)
                if heap_max:
                    visited[heap_max[0][1]] = False
                    heapq.heappop(heap_max)
            else:  # delete min
                while heap_min and not visited[heap_min[0][1]]:
                    heapq.heappop(heap_min)
                if heap_min:
                    visited[heap_min[0][1]] = False
                    heapq.heappop(heap_min)

    while heap_max and not visited[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap_min and not visited[heap_min[0][1]]:
        heapq.heappop(heap_min)

    if not heap_max and not heap_min:
        print("EMPTY")
    else:
        print(f'{-heap_max[0][0]} {heap_min[0][0]}')
