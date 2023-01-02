import sys
input = sys.stdin.readline

L = int(input())
input_string = input()
answer = 0

for i in range(L):
    char_to_int = ord(input_string[i]) - 96
    answer += char_to_int * (31 ** i)

print(answer % 1234567891)
