def solution(numbers, hand):
    answer = ''
    left = [0, 3]
    right = [2, 3]
    hand = hand[0].upper()
    for curr in numbers:
        print(f'{left} {right}')
        if curr == 0:
            curr = 11
        if curr % 3 == 2:
            dis_L = (left[0] - 1) ** 2 + (left[1] - (curr + 1) // 3 + 1) ** 2
            dis_R = (right[0] - 1) ** 2 + (right[1] - (curr + 1) // 3 + 1) ** 2
            if dis_L == dis_R:
                answer += hand[0]
            elif dis_L < dis_R:
                answer += 'L'
                left = [1, (curr + 1) // 3 - 1]
            else:
                answer += 'R'
                right = [1, (curr + 1) // 3 - 1]
        elif curr % 3 == 1:
            answer += 'L'
            left = [0, ((curr + 2) // 3) - 1]
        else:
            answer += 'R'
            right = [2, (curr // 3) - 1]
    return answer
  
