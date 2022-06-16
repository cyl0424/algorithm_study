num = int(input())
words = set()

for _ in range(num):
    words.add(input())

words = list(words)
words.sort()
words.sort(key=len)

for i in words:
    print(i)