def solution(answers):
    answer = []
    
    st_1 = [1, 2, 3, 4, 5]
    st_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1 = 0
    s2 = 0
    s3 = 0
    
    for i, a in enumerate(answers):
        if a == st_1[i%len(st_1)]:
            s1 += 1
        if a == st_2[i%len(st_2)]:
            s2 += 1
        if a == st_3[i%len(st_3)]:
            s3 += 1
    
    max_score = max(s1, s2, s3)
    
    if s1 == max_score:
        answer.append(1)
    if s2 == max_score:
        answer.append(2)
    if s3 == max_score:
        answer.append(3)
        
    return answer