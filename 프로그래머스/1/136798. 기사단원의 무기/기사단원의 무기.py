def solution(number, limit, power):
    answer = 0
    
    for n in range(1, number + 1):
        cnt = 0
        
        if n == 1:
            cnt = 1
        else:
            sqrt_n = int(n ** 0.5)
            for i in range(1, sqrt_n + 1):
                if n % i == 0:
                    cnt += 1
                    if i != n // i:
                        cnt += 1

        if cnt > limit:
            answer += power
        else:
            answer += cnt
    
    return answer
