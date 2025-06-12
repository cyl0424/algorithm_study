def solution(video_len, pos, op_start, op_end, commands):
    answer = []
    cur_m, cur_s = map(int, pos.split(':'))
    cur_time = cur_m * 60 + cur_s
    
    end_m, end_s = map(int, video_len.split(':'))
    end_time = end_m * 60 + end_s
    
    op_s_m, op_s_s = map(int, op_start.split(':'))
    op_s_time = op_s_m * 60 + op_s_s
    
    op_e_m, op_e_s = map(int, op_end.split(':'))
    op_e_time = op_e_m * 60 + op_e_s
    
    # 현재 위치가 오프닝 중일 경우
    if op_s_time <= cur_time <= op_e_time:
            cur_time = op_e_time
    
    # 각 command 처리
    for command in commands:
        if command == "prev":
            cur_time = max(0, cur_time-10)
        else:
            cur_time = min(end_time, cur_time+10)
        
        if op_s_time <= cur_time <= op_e_time:
            cur_time = op_e_time
    
    return f"{cur_time // 60 :02d}:{cur_time % 60 :02d}"