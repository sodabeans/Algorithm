hr, min = map(int, input().split())
C = int(input())

min = min + C
while min >= 60:
    hr = hr + 1
    min = min - 60

if hr >= 24:
    hr = hr - 24

print("{} {}".format(hr, min))