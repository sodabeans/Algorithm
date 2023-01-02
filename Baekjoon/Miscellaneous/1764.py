import sys
input = sys.stdin.readline

N, M = map(int, input().split())
people = dict()
cnt = 0

for _ in range(N):
    not_heard = input().rstrip()
    people[not_heard] = 0

for _ in range(M):
    not_seen = input().rstrip()
    if not_seen in people:
        cnt += 1
        people[not_seen] = 1
    else:
        people[not_seen] = 0

print(cnt)
for p in sorted(people.keys()):
    if people[p] == 1:
        print(p)
