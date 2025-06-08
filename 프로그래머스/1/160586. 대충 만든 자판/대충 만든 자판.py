def solution(keymap, targets):
    char_min_press = {}
    
    for key_idx, key in enumerate(keymap):
        for char_idx, char in enumerate(key):
            press_count = char_idx + 1
            
            if char not in char_min_press:
                char_min_press[char] = press_count
            else:
                char_min_press[char] = min(char_min_press[char], press_count)
    
    answer = []
    
    for target in targets:
        total_press = 0
        possible = True
        
        for char in target:
            if char in char_min_press:
                total_press += char_min_press[char]
            else:
                possible = False
                break
        
        if possible:
            answer.append(total_press)
        else:
            answer.append(-1)
    
    return answer
