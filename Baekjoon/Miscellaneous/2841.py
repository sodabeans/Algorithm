import sys
input = sys.stdin.readline

N, P = map(int, input().split())
ans = 0
guitar = [list() for _ in range(6)]

for _ in range(N):
    string, flat = map(int, input().split())
    if len(guitar[string-1]) == 0 or guitar[string-1][-1] < flat:
        guitar[string - 1].append(flat)
        ans += 1
    elif guitar[string-1][-1] > flat:
        while guitar[string-1][-1] > flat:
            guitar[string-1].pop()
            ans += 1
            if len(guitar[string-1]) == 0:
                break
        if guitar[string-1] and guitar[string-1][-1] == flat:
            continue
        guitar[string-1].append(flat)
        ans += 1

print(ans)