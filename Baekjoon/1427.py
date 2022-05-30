import sys
input = sys.stdin.readline

input_string = list(input().rstrip())
input_string.sort(reverse=True)

print(''.join(input_string))
