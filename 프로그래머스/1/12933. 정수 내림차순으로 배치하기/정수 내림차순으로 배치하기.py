def solution(n):
    answer = int(''.join(sorted(str(n), reverse=True)))
    print(sorted(str(n), reverse=True))
    return answer