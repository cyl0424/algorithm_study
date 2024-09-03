dishes = list(input())
height = 10

before = dishes[0]

for now in dishes[1:]:
    if (before == now):
        height += 5
    else:
        height += 10
    
    before = now

print(height)