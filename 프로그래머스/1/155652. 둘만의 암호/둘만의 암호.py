from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    alpha = set(ascii_lowercase) - set(skip)
    alpha = sorted(alpha)
    l = len(alpha)

    alpha_num = {a:idx for idx, a in enumerate(alpha)}

    for c in s:
        result += alpha[(alpha_num[c] + index) % l]

    return result