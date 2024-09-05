raw = input()
nums = raw.split("-")
sum_nums = []

for i in nums:
    tmp = list(map(int, i.split('+')))
    sum_nums.append(sum(tmp))

res = sum_nums.pop(0)

if (len(sum_nums) > 0):
    for n in sum_nums:
        res -= n

print(res)