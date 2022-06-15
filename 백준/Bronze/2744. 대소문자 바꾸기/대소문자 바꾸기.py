var = input()
new = []

for i in var:
    if i.isupper():
        new.append(i.lower())
    elif i.islower():
        new.append(i.upper())
    else:
        new.append(i)

print(''.join(new))