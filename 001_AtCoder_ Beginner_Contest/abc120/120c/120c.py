#21:59:10~
S = input()
rtn = 0
first = True
i = len(S) - 2

while i >= 0:
# for i in range(len(S) - 2,0,-1):
    if S[i] != S[i + 1]:
        rtn += 2
        if len(S) == i + 2:
            S = S[:i]
            i -= 1
        else:
            S = S[:i] + S[i + 2:]
    i -= 1

print(rtn)