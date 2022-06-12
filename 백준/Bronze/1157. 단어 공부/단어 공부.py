A = input().upper()
chars = {}

for i in A:
    if i in chars.keys():
        chars[i] += 1
    else:
        chars[i] = 1

result = max(chars.values())
answer = ''
cnt = 0

for k, v in chars.items():
    if v == result:
        answer = k
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(answer)