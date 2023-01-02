import sys

input = sys.stdin.readline

N = int(input())

members_age = dict()
members_name = dict()

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    members_age[i] = age
    members_name[i] = name

members_new = sorted(members_age.items(), key=lambda item: item[1])

for i, age in members_new:
    print(f'{age} {members_name[i]}')