def solution(common):
    if 2 * common[1] == common[2] + common[0]:
        return common[-1] + (common[1] - common[0])
    else:
        r = (common[1] // common[0])
        return common[-1] * r