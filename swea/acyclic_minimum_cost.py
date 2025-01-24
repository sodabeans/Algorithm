T = int(input())

for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    answer = 0
    costs = [float('inf') for _ in range(N + 1)]
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort()
    costs[0] = 0
    for start, end, cost in edges:
        costs[end] = min(costs[end], costs[start] + cost)
    print(f"#{test_case} {costs[-1]}")
  
