def solution(phone_number):
    cnt = len(phone_number)-4
    answer = '*' * cnt + phone_number[cnt:]
    return answer