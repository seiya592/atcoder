#22:10:20~
S = input()
l = (len(S) + 1) // 2 if len(S) % 2 == 0 else ((len(S) - 1) // 2)
rtn = 0
for i in range(l):
    if S[i] != S[(i * - 1) - 1]:
        rtn += 1

print(rtn)