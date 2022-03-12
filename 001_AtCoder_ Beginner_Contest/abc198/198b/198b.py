# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N = input()

if N == '0':
    print('Yes')
    exit()

while True:
    if N[-1] == '0':
        N = N[:-1]
    else:
        break

while True:
    if len(N) > 1:
        if N[0] == N[-1]:
            N = N[1:-1]
        else:
            print('No')
            break
    else:
        print('Yes')
        break