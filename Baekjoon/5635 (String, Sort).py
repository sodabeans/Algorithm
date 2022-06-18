import sys
input = sys.stdin.readline

n = int(input())
birthday = []

for _ in range(n):
    personal_info = input().rstrip().split()
    date = personal_info[3]
    if int(personal_info[2]) < 10:
        date += "0"
    date += personal_info[2]
    if int(personal_info[1]) < 10:
        date += "0"
    date += personal_info[1]
    birthday.append([int(date), personal_info[0]])

birthday.sort()
print(birthday[-1][1])
print(birthday[0][1])
