N = int(input())
listS = set(input() for i in range(N))

rtn = 'satisfiable'


for listSS in listS:
    if '!' in listSS:
        if listSS[1:] in listS:
            rtn = listSS[1:]
            break
    else:
        if '!' + listSS in listS:
            rtn = listSS
            break

print(rtn)
