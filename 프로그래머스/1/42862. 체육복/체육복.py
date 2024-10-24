def solution(n, lost, reserve):
    answer = n
    n_lost = sorted(set(lost) - set(reserve))
    n_reserve = sorted(set(reserve) - set(lost))
    
    for i in n_lost:
        if i-1 in n_reserve:
            n_reserve.remove(i-1)
        elif i+1 in n_reserve:
            n_reserve.remove(i+1)
        else:
            answer -= 1
    return answer