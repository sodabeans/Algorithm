from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    entries = deque()
    k = int(input())
    for _ in range(k):
        calc, n = map(str, input().split())
        n = int(n)
        if calc == 'I':
            entries.append(n)
        else:
            if entries:
                entries = deque(sorted(entries))
                if n == 1:
                    entries.pop()
                else:
                    entries.popleft()
    if entries:
        print(f'{entries[-1]} {entries[0]}')
    else:
        print('EMPTY')
