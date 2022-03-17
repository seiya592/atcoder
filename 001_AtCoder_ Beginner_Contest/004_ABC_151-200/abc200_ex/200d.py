S = input()

def dell(arr, arr2):
    i = min(len(arr), len(arr2))

    if len(arr) == 0 or len(arr2) == 0:
        return arr + arr2

    for j in range(i):
        if arr[-1 * (j + 1)] != arr2[j]:
            break

    if j == 0:
        rtn = arr + arr2
    else:
        rtn = arr[:-1 * (j + 1)] + arr2[j + 1:]

    return rtn

rtn = ""
tmp = ""
tmp2 = ""
flg = True
for i in range(len(S)):

    if S[i] == 'R':
        flg = not flg
    else:
        if flg == True:
            if tmp != "" and S[i] == tmp[-1]:
                tmp = tmp[:-1]
            else:
                tmp = tmp + S[i]
        else:
            if tmp2 != "" and S[i] == tmp2[-1]:
                tmp2 = tmp2[:-1]
            else:
                tmp2 = tmp2 + S[i]

if flg == True:
    rtn = dell(tmp2[::-1],tmp)
else:
    rtn = dell(tmp[::-1],tmp2)

print(rtn)