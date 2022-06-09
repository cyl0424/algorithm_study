n = int(input())

for _ in range(n):
    cnt = 0
    scores = list(map(int, input().split()))[1:]
    avg = sum(scores)/len(scores)
    for i in scores:
        if i > avg:
            cnt += 1
    print(f"{cnt/len(scores)*100:.3f}%")