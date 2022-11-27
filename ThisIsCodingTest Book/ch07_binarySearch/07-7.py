import sys
input = sys.stdin.readline

_ = int(input())
store = set(list(map(int, input().split())))
_ = int(input())
guest = list(map(int, input().split()))

for curr in guest:
    if curr in store:
        print('yes', end=' ')
    else:
        print('no', end=' ')
