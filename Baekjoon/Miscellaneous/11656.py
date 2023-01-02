import sys
input = sys.stdin.readline

input_string = input().rstrip()
input_list = []

for i in range(len(input_string)):
    input_list.append(input_string[i:])

input_list.sort()

for element in input_list:
    print(element)
