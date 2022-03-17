#19:01:30~
N = input()
rtn = -1
for i in range(1,2 ** len(N) + 1):
    tmp = 0
    rtntmp = 0
    for j in range(0,len(N)):
        if (i >> j) & 1 == 1:
            tmp += int(N[j])
            rtntmp += 1

    if tmp % 3 == 0 and tmp != 0:
        rtn = max(rtn,rtntmp)

print(len(N) - rtn if rtn != -1 else -1)