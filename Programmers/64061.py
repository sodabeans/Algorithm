def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1]:
                if len(basket) > 0 and basket[-1] == board[i][move - 1]: # check before adding to basket so that pop only once
                    answer += 2
                    basket.pop(-1)
                    board[i][move - 1] = 0
                    break
                else:
                    basket.append(board[i][move - 1])
                    board[i][move - 1] = 0
                    break
    """
    # first trial - got answer but had to create another board (just for me to understand the problem better)
    basket = []
    size_board = len(board)
    curr = [[] for _ in range(size_board)]
    
    for j in range(size_board):
        for i in range(size_board):
            if board[i][j]:
                curr[j].append(board[i][j])
    
    for move in moves:
        if not curr[move - 1]:
            continue
        basket.append(curr[move - 1].pop(0))
        if len(basket) < 2:
            continue
        for idx in range(len(basket) - 1):
            if basket[idx] == basket[idx + 1]:
                basket.pop(idx)
                basket.pop(idx)
                answer += 2
    """
    return answer
    
