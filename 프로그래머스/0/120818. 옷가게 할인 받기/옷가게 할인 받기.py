def solution(price):
    if price >= 500_000:
        return int(price * 0.80)
    elif price >= 300_000:
        return int(price * 0.90)
    elif price >= 100_000:
        return int(price * 0.95)
    else:
        return price