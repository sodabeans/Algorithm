import re
from itertools import permutations


def calculation(operation_order, numbers_list, operation_list):
    i = 0

    while len(numbers_list) > 1:
        curr_operation = operation_order[i]
        while curr_operation in operation_list:
            idx = operation_list.index(curr_operation)
            operation = operation_list.pop(idx)
            num1 = numbers_list.pop(idx)
            num2 = numbers_list.pop(idx)
            if operation == '+':
                numbers_list.insert(idx, num1 + num2)
            elif operation == '-':
                numbers_list.insert(idx, num1 - num2)
            else:
                numbers_list.insert(idx, num1 * num2)
        i += 1

    return abs(numbers_list[0])


def solution(expression):
    answer = 0
    num_list = [int(x) for x in re.split("[^0-9]", expression)]
    oper_list = [x for x in re.split(r'[0-9]+', expression) if x]
    oper_priorities = list(map(list, permutations(set(oper_list))))

    for curr_order in oper_priorities:
        curr_num_list = num_list.copy()
        curr_oper_list = oper_list.copy()
        result = calculation(curr_order, curr_num_list, curr_oper_list)
        answer = max(result, answer)

    return answer
