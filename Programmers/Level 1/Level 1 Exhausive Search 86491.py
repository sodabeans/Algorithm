def solution(sizes):
    w = 0
    h = 0
    for x, y in sizes:
        if x > y:
            w = max(w, x)
            h = max(h, y)
        else:
            w = max(w, y)
            h = max(h, x)
    return w * h
