def solution(babbling):
    answer = 0
    sayings = sorted(["aya", "ye", "woo", "ma"])
    
    for bab in babbling:
        tmp = ""
        for saying in sayings:
            if bab.find(saying) >= 0:
                tmp += saying
            
        if len(tmp) == len(bab):
            answer += 1
    return answer