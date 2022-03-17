# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

#20:59:20~
N = int(input())
S = [input() for i in range(N)]
AC = 0
TLE = 0
WA = 0
RE = 0
for s in S:
    if s == 'AC':
        AC += 1
    elif s == 'TLE':
        TLE += 1
    elif s == 'WA':
        WA +=1
    else:
        RE += 1

print('AC x',AC)
print('WA x' ,WA)
print('TLE x' ,TLE)
print('RE x' ,RE)

