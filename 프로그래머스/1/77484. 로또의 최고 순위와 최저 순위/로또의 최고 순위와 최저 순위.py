def solution(lottos, win_nums):
    answer = []
    winning = [6, 6, 5, 4, 3, 2, 1]
    
    lottos.sort()
    zero = lottos.count(0)
    
    lottos = lottos[zero:]
    tmp = 0
    
    for l in lottos:
        if l in win_nums:
            tmp += 1
        
    answer = [winning[tmp+zero], winning[tmp]]
    
    return answer