colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
col1 = input()
col2 = input()
col3 = input()

res = int(str(colors.index(col1)) + str(colors.index(col2)))*pow(10, colors.index(col3))

print(res)