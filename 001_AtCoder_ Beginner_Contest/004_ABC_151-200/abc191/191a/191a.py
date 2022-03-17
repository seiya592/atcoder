V,T,S,D = map(int,input().split())

tomeiMin = V * T
tomeiMax = V * S

if tomeiMin <= D and D <= tomeiMax:
    print('No')
else:
    print('Yes')

