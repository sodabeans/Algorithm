def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans_one = 0
    ans_two = 0
    ans_three = 0
    ans_list = []
    
    for i in range(len(answers)):
        if (answers[i] == one[i % 5]):
            ans_one = ans_one + 1
        if (answers[i] == two[i % 8]):
            ans_two = ans_two + 1
        if (answers[i] == three[i % 10]):
            ans_three = ans_three + 1

    ans_list.append(ans_one)
    ans_list.append(ans_two)
    ans_list.append(ans_three)
    
    max_ans = max(ans_list)
    
    if max_ans == ans_one:
        answer.append(1)
    if max_ans == ans_two:
        answer.append(2)
    if max_ans == ans_three:
        answer.append(3)
    
    return answer
