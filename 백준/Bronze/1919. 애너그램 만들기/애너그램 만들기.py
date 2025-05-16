from collections import Counter
import sys
input = sys.stdin.readline

word1 = list(input().strip())
word2 = list(input().strip())

c1 = Counter(word1)
c2 = Counter(word2)

delete_count = sum((c1 - c2).values()) + sum((c2 - c1).values())
print(delete_count)