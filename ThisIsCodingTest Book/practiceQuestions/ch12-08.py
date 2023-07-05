import sys
input = sys.stdin.readline

input_string = list(input().strip())
num = 0

input_string = sorted(input_string)

while True:
    if input_string[0].isdigit():
        num += int(input_string[0])
        input_string.pop(0)
    else:
        break

for char in input_string:
    print(char, end="")
print(num)
