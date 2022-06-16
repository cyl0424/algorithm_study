alphas = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
call = input()
res = 0

for i in call:
    for j in alphas:
        if i in j:
            res += alphas.index(j) + 3

print(res)