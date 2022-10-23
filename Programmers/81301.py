def solution(s):
    answer = 0
    num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx in range(10):
        s = s.replace(num_words[idx], str(idx))
    return int(s)
