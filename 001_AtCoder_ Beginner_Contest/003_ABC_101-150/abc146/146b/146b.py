#21:41:25~
N = int(input())
S = input()
rtn = []
for i in range(len(S)):
    if ord(S[i]) + N > 90:
        rtn.append(chr(ord(S[i]) + N - 26))
    else:
        rtn.append(chr(ord(S[i]) + N))

print(''.join(rtn))