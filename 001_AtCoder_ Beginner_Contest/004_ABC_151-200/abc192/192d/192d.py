X = input()
M = int(input())

d = int(sorted(X, reverse=True)[0])
rtn = 0

if len(X) == 1:
    print('1' if M >= int(X) else '0')
    exit()

tmp2 = 0
for i in range(len(X)):
    tmp2 += int(X[((i + 1) * - 1)]) * ((d + 1) ** i)
if tmp2 > M:
    print(0)
    exit()


def nibugi(Min, Max, M, X):
    center = (Min + Max) // 2
    tmp = 0
    tmp1 = 0
    for i in range(len(X)):
        tmp += int(X[((i + 1) * - 1)]) * (center ** i)

    for i in range(len(X)):
        tmp1 += int(X[((i + 1) * - 1)]) * ((center + 1) ** i)

    if tmp <= M < tmp1:
        return center
    elif tmp > M:
        return nibugi(Min, center, M, X)
    elif tmp < M:
        if center == Min:
            return center + 1
        return nibugi(center, Max, M, X)


rtn = nibugi(d + 1, M, M, X) - d

print(rtn)