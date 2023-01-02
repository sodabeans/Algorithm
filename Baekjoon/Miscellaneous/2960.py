import sys
input = sys.stdin.readline

N, K = map(int, input().split())

prime = [True for _ in range(N + 1)]

p = 2
cnt = 0
while (p <= N):
    if prime[p] == True:
        cnt += 1
        if cnt == K:
            print(p)
        for i in range(p * p, N + 1, p):
            if prime[i]:
                prime[i] = False
                cnt += 1
                if cnt == K:
                    print(i)
    p += 1
