from collections import Counter
import sys
input = sys.stdin.readline

stickers = Counter(input().rstrip())
mobis = Counter("MOBIS")

if sum((mobis-stickers).values()) > 0:
    print("NO")
else:
    print("YES")