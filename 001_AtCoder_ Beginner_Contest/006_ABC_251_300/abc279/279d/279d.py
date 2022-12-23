"""
2022/11/26 20:58:17
"""
import math


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**20


A,B = IIS()
ans = INF
for x in range(0,10000000):
    ans = min(ans,B * x + (A / math.sqrt(x + 1)))
print(ans)

# #数字をxにするのはは効率がいいか悪いか
# def calc(x):
#     y = x-1
#     if B * x + (A / math.sqrt(x + 1)) < B * y + (A/math.sqrt(y+1)):
#         return True
#     else:
#         return False
#
# ok = 0
# ng = 10**20+1
# while abs(ok-ng) > 1:
#     mid = (ok+ng)//2
#     if calc(mid):
#         ok = mid
#     else:
#         ng = mid
# ans = INF
# for i in range(max(ok-10000,0),ng+10000):
#     x = i
#     ans = min(ans,B * x + (A / math.sqrt(x + 1)))
#
# def calc2(x):
#     y = x-1
#     if B * x + (A / math.sqrt(x + 1)) >= B * y + (A/math.sqrt(y+1)):
#         return True
#     else:
#         return False
#
# ok = 10**20+1
# ng = 0
# while abs(ok-ng) > 1:
#     mid = (ok+ng)//2
#     if calc2(mid):
#         ok = mid
#     else:
#         ng = mid
# # ans = INF
# for i in range(max(ng-10000,0),ok+10000):
#     x = i
#     ans = min(ans,B * x + (A / math.sqrt(x + 1)))
# print(ans)
#
#
#


# for i in range(1,n):
#     s.append(s[-1]+a[i])
#
# #(1)最小にしたい関数fを定義する
# def f(c,i):
#     global n,a,s
#     return s.append(s[-1]+a[i])
#
# #(1)
# def g(c,i):
#     global n,a,s
#     return abs((s[c]-s[i])-(s[n-1]-s[c]))
#
# ans=[]
# for i in range(1,n-2):
#     ans_=[]
#
#     #(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
#     #ここではインデックスの値になる
#     l,r=0,10**18
#     #(3)整数なので、r=l,l+1,l+2のいずれかになれば良い
#     #逆にr>=l+3の場合はrとlの差をもっと小さくできる
#     while l+2<r:
#         #(4)三等分点(小数部分は切り捨て)
#         c1=l+(r-l)//3
#         c2=r-(r-l)//3
#         #(5)更新を行う
#         if f(c1,i)<f(c2,i):
#             r=c2
#         else:
#             l=c1
#     #(6)最終的に求めるのはl~rのうち関数fの値が最小になる要素
#     x=sorted([(f(j,i),j) for j in range(l,r+1)])[0][1]
#     ans_.append(s[x])
#     ans_.append(s[i]-s[x])
#
#     #右側決める
#
#     #(2)
#     l,r=i+1,n-1
#     #(3)
#     while l+2<r:
#         #(4)
#         c1=l+(r-l)//3
#         c2=r-(r-l)//3
#         #(5)
#         if g(c1,i)>g(c2,i):
#             l=c1
#         else:
#             r=c2
#     #(6)
#     x=sorted([(g(j,i),j) for j in range(l,r+1)])[0][1]
#     ans_.append(s[x]-s[i])
#     ans_.append(s[n-1]-s[x])
#
#     ans.append(max(ans_)-min(ans_))
# print(min(ans))



# #(1)最小にしたい関数fを定義する
# def f(x):
#
#     return B * x + (A/math.sqrt(x+1))
#
# #(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
# l,r=0,10**18
# #(3)誤差が10^-8を下回るまでwhile文を回す
# while l+2<r:
#     #(4)オーバーフローしないように以下のように三等分点を置く
#     c1=l+(r-l)//3
#     c2=r-(r-l)//3
#     #(5)更新を行う
#     if f(c1)<f(c2):
#         r=c2
#     else:
#         l=c1
#
#
# #(6)最終的に出力するのはl,rのどちらでも良い
# ans = INF
# for i in range(l,r+1):
#     ans = min(ans,f(i))
#
#
# #(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
# l,r=10**18,0
# #(3)誤差が10^-8を下回るまでwhile文を回す
# while l+2<r:
#     #(4)オーバーフローしないように以下のように三等分点を置く
#     c1=l+(r-l)//3
#     c2=r-(r-l)//3
#     #(5)更新を行う
#     if f(c1)>f(c2):
#         l=c2
#     else:
#         r=c1
#
#
# #(6)最終的に出力するのはl,rのどちらでも良い
# for i in range(l,r+1):
#     ans = min(ans,f(i))
#
#
# print(ans)