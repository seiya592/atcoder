def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
S = I()

w_num = [0]
for i in range(N):
    if S[i] == 'W':
        w_num.append(w_num[i] + 1)
    else:
        w_num.append(w_num[i])

ans = 10**100
for i in range(N):
    # 西にいる人で東を向く人
    tmp = w_num[i]
    # 東にいる人で西を向く人
    #      東にいる人　　　- 西を向いている人　→　東にいる人で西を向く人
    tmp += ((N - 1) - i) - (w_num[N]-w_num[i+1])
    ans = min(ans, tmp)
print(ans)