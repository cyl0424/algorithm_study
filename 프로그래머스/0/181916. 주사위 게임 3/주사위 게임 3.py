def solution(a, b, c, d):
    dices = [a, b, c, d]
    sets = list(set(dices))
    
    if len(sets) == 1:
        return 1111 * sets[0]
    elif len(sets) == 2 and dices.count(sets[0]) == 1:
        return (sets[0] + 10 * sets[1]) ** 2
    elif len(sets) == 2 and dices.count(sets[0]) == 3:
        return (sets[1] + 10 * sets[0]) ** 2
    elif len(sets) == 2 and dices.count(sets[0]) == 2:
        return (sets[0] + sets[1]) * abs(sets[0] - sets[1])
    elif len(sets) == 3:
        if dices.count(sets[0]) == 2:
            return sets[1] * sets[2]
        elif dices.count(sets[1]) == 2:
            return sets[0] * sets[2]
        elif dices.count(sets[2]) == 2:
            return sets[1] * sets[0]
    else:
        return min(sets)
        