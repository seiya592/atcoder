# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

X = input()
i = X.find('.')

if i == -1:
    if X == '0':
        print(0)
        exit()
    else:
        print(int(X))
        exit()

XX = X[:i]
print(int(XX))