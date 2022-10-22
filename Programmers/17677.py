def solution(str1, str2):
    answer = 0
    str_list1 = [str1[idx:idx+2].lower() for idx in range(len(str1) - 1) if str1[idx:idx+2].isalpha()]
    str_list2 = [str2[idx:idx+2].lower() for idx in range(len(str2) - 1) if str2[idx:idx+2].isalpha()]
    # intersection = [x for x in str_list1 + str_list2 if x in str_list1 and x in str_list2]
    # numerator = int(len(intersection) / 2)
    # denominator = len(str_list1) + len(str_list2) - numerator
    # if denominator == 0:
    #     return 65536
    # answer = int(numerator * 65536 / denominator)
    intersection = 0
    total = len(str_list1) + len(str_list2)
    for idx in range(len(str_list1)):
        if str_list1[idx] in str_list2:
            str_list2.remove(str_list1[idx])
            total -= 1
            intersection += 1
    if total == 0:
        answer = 65536
    else:
        answer = int(intersection * 65536 / total)
    return answer
