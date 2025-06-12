def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    hd = ((360 / 12) / 60) / 60 # 초당 시침 이동각도
    md = ((360) / 60) / 60 # 초당 분침 이동 각도
    sd = 360 / 60 # 초당 초침 이동 각도
    
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2
    
    if start == 0 or start == 12 * 3600:
        answer += 1
    
    while start < end:
        cur_h = start * hd % 360
        cur_m = start * md % 360
        cur_s = start * sd % 360
        
        start += 1
        
        next_h = 360 if start * hd % 360 == 0 else start * hd % 360
        next_m = 360 if start * md % 360 == 0 else start * md % 360
        next_s = 360 if start * sd % 360 == 0 else start * sd % 360
        
        if cur_h > cur_s and next_h <= next_s: # s가 h와 겹쳐진 후 지나감
            answer += 1
        if cur_m > cur_s and next_m <= next_s: # s가 m과 겹쳐진 후 지나감
            answer += 1
        if next_h == next_s and next_m == next_s: # 분침, 시침, 초침이 동시에 겹침
            answer -= 1
            
    return answer