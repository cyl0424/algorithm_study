def solution(bandage, health, attacks):
    hp = health
    time = 0 # 이전에 공격당한 시간
    lasting = 0
    
    t, x, y = bandage
    
    for attack in attacks:
        lasting = attack[0] - time - 1
        hp = min(health, hp + lasting * x)
        
        if lasting >= t:
            hp = min(health, hp + (lasting // t) * y)
            
        hp -= attack[1]
        time = attack[0]
        lasting = 0
        
        if hp <= 0:
            hp = -1
            break
            
    return hp