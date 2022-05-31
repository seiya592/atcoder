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
INF = 10**20
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

N,A,B = IIS()

#Aの倍数の数
N_sum = N*(N+1)//2
a_count = N // A
b_count = N // B

a_sum = (a_count*((A*a_count)+A))//2
b_sum = (b_count*((B*b_count)+B))//2

AB = my_lcm(A,B)
ab_count = N // AB
ab_sum = (ab_count*((AB*ab_count)+AB))//2

print(N_sum-(a_sum+b_sum)+ab_sum)

# A_sum = A+(A*a_count) * (a_count//2)
# if a_count % 2 == 1:
#     A_sum += (A+(A*a_count))//2
#
# B_sum = B+(B*b_count) * (b_count//2)

# if b_count % 2 == 1:
#     B_sum += (B + (B * b_count)) // 2

# ab_count = N // (A*B)
#
# AB_sum = ((A*B)+((A*B)*ab_count)) * (ab_count//2)
# if ab_count % 2 == 1:
#     AB_sum += ((A*B)+((A*B)*ab_count)) // 2
# if A != B and not(A % B == 0 or B % A == 0):
#     print(N_sum-(a_sum+b_sum)+ab_sum)
# elif not A % B == 0:
#     print(N_sum-a_sum)
# else:
#     print(N_sum-b_sum)
# # #
# ans = 0
# t1= 0
# t2 = 0
# for i in range(1,107+1):
#     if i % 8 == 0:
#         t1+=i
#     elif i % 4 == 0:
#         t2 += i
#     else:
#         ans += i
# print(ans)