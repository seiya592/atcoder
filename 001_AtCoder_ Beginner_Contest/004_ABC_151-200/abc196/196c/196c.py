# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

N = input()

if int(N) < 10:
    print(0)
    exit()

if len(N) % 2 != 0:
    N = str((10 ** (len(N) - 1)) -1)

Nh = N[:len(N)//2]
Nl = N[len(N)//2:]

if Nh <= Nl:
    print(Nh)
else:
    print(int(Nh)-1)