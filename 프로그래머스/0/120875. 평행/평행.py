def solution(dots):
    a, b, c, d = dots
    
    if (a[0] - b[0]) / (a[1] - b[1]) == (c[0] - d[0]) / (c[1] - d[1]):
        return 1
    elif (a[0] - c[0]) / (a[1] - c[1]) == (b[0] - d[0]) / (b[1] - d[1]):
        return 1
    elif (a[0] - d[0]) / (a[1] - d[1]) == (c[0] - b[0]) / (c[1] - b[1]):
        return 1
    
    return 0