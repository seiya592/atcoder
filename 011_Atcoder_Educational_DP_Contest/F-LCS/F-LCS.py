# https://atcoder.jp/contests/dp/tasks/dp_f
s = input()
t = input()

S = len(s)
T = len(t)
comp = []
for i in range(S+1):
    comp.append([0] * (T+1))

for i in range(1,S+1):
    for j in range(1, T+1):
        comp[i][j] = max(comp[i-1][j], comp[i][j-1])
        if s[i-1] == t[j-1]:
            comp[i][j] = max(comp[i-1][j-1] + 1, comp[i][j])

ans = ''
len = comp[S][T]
i = S-1
j = T-1
while len>0:
    if s[i] == t[j]:
        ans = s[i] + ans
        i -=1
        j -=1
        len -=1
    elif comp[i+1][j+1] == comp[i][j+1]:
        i -=1
    else:
        j -=1

print(ans)