def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


X,A,D,N = IIS()


if D == 0:
    print(abs(X-A))
    exit()

ok = 0
ng = N-1


if A <= X <= A+D*N or A >= X >= A+D*N:
    if D > 0:
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if A+(D*mid) <= X:
                ok = mid
            else:
                ng = mid

        ans = min(abs(X-(A+D*ok)), abs(X-(A+D*ng)))
    else:
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if A + (D * mid) >= X:
                ok = mid
            else:
                ng = mid

        ans = min(abs(X - (A + D * ok)), abs(X - (A + D * ng)))

else:
    if X < A and X < A+N*D:
        if D > 0:
            ans = abs(X - A)
        else:
            ans = abs(X - (A + (N-1) * D))
    elif X > A and X > A+N*D:
        if D > 0:
            ans = abs(X -(A+(N-1)*D))
        else:
            ans = abs(X - A)
    else:
        raise ValueError

print(ans)
# t = X+A
#
# tt = abs(t // D)
# # tt2 = (t // D)+1
# # tt3 = ((t // D)-1) * D
#
# ans = abs(tt * D + A + X)
# ans2 = abs((tt+1) * D + A + X)
# ans3 = abs(tt * D + A - X)
# ans4 = abs((tt+1) * D + A - X)
# ans5 = abs((tt-1) * D + A + X)
# ans6 = abs((tt-1) * D + A - X)
#
#
#
# # ans = min(abs(tt+(A%D)-X),abs(tt2+(A%D)-X),abs(tt3+(A%D)-X))
# if A <= X <= (A+D*N) or A >= X >= (A+D*N):
#     print(min(ans,ans2,ans3,ans4,ans5,ans6))
# else:
#     print(min(abs(X-A),abs(X-(A+D*N))))


# t = X + A
# t2 = t - D
#
#
# # if X > 0:
# t = min(t,A+D*N)
# t2 = min(t2,A+D*N)
# # else:
# #     t = max(t,A+D*N)
# #     t2 = max(t,A+D*N)
#
# print(min(abs(X-t2),abs(X-t)))