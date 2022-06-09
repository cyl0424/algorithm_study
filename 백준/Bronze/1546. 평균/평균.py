n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_scores = []

for i in scores:
    new_scores.append(i/max_score*100)

print(sum(new_scores)/len(new_scores))