S = input()

S = S.translate(str.maketrans({
    'A': '0',
    'C': '0',
    'G': '0',
    'T': '0'
}))

cnt = 0
rtn = 0
for i in range(len(S)):
    if S[i] == '0':
        cnt += 1
    else:
        if cnt > rtn:
            rtn = cnt
        cnt = 0

if cnt > rtn:
    rtn = cnt

print(rtn)

# 12:04
