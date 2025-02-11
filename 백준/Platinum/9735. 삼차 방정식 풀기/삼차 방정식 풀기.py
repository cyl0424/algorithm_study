import math

def find_factor(x):
    """x의 모든 약수를 찾아 반환"""
    factor_set = set()
    x = abs(x)
    end = int(math.sqrt(x))
    for i in range(1, end + 1):
        if x % i == 0:
            factor_set.update({i, x // i, -i, -(x // i)})
    return factor_set

def synthetic_division(coeffs, root):
    """조립제법을 사용하여 다항식을 한 차수 낮춤"""
    new_coeffs = [coeffs[0]]  # 첫 번째 계수 그대로 유지
    for i in range(1, len(coeffs) - 1):
        new_coeffs.append(new_coeffs[-1] * root + coeffs[i])
    remainder = new_coeffs[-1] * root + coeffs[-1]
    return new_coeffs, remainder

def solve_cubic(a, b, c, d):
    """3차 방정식 ax^3 + bx^2 + cx + d = 0의 실근을 찾음"""
    result = set()
    
    # d의 약수를 a의 약수로 나누어 근 후보 생성
    a_factors = find_factor(a)
    d_factors = find_factor(d)
    if d == 0:
        result.add(0)
        a, b, c = a, b, c  # 2차 방정식 해결을 위해 조립제법 안 함
    else:
        for factor in d_factors:
            for a_factor in a_factors:
                x = factor / a_factor
                _, remainder = synthetic_division([a, b, c, d], x)
                if abs(remainder) < 1e-7:
                    result.add(x)
                    # 조립제법 적용하여 2차 방정식 계수 생성
                    a, b, c = synthetic_division([a, b, c, d], x)[0]
                    break  # 하나 찾았으면 종료
            if len(result) > 0:
                break  # 조립제법 한 번 실행하면 더 이상 실행할 필요 없음

    # 남은 2차 방정식 ax^2 + bx + c = 0을 풀이
    if a != 0:
        D = b**2 - 4 * a * c
        if D == 0:
            result.add(-b / (2 * a))
        elif D > 0:
            sqrt_D = math.sqrt(D)
            result.add((-b + sqrt_D) / (2 * a))
            result.add((-b - sqrt_D) / (2 * a))

    return sorted(result)

# 입력 처리
num = int(input())

for _ in range(num):
    a, b, c, d = map(int, input().split())
    roots = solve_cubic(a, b, c, d)
    print(" ".join(f"{root:.4f}" for root in roots))
