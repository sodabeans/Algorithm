def solution(numbers, hand):
    answer = ''
    hand = hand[0].upper()
    
    L_row = 3
    L_col = 0
    R_row = 3
    R_col = 2
    
    for n in numbers:
        if n == 0:
            n = 11

        if n % 3 == 1:  # first column
            answer += 'L'
            L_row = ((n + 2) // 3) - 1
            L_col = 0
        elif n % 3 == 0:  # third column
            answer += 'R'
            R_row = (n // 3) - 1
            R_col = 2
        else:  # second column
            row = ((n + 1) // 3) - 1
            dis_L = abs(L_row - row) + abs(L_col - 1)
            dis_R = abs(R_row - row) + abs(R_col - 1)
            if dis_L == dis_R:
                answer += hand
                if hand == 'L':
                    L_row = row
                    L_col = 1
                else:
                    R_row = row
                    R_col = 1
            elif dis_L > dis_R:
                answer += 'R'
                R_row = row
                R_col = 1
            else:
                answer += 'L'
                L_row = row
                L_col = 1
    
    return answer
