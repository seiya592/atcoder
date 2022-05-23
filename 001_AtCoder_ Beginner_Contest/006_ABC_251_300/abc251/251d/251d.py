def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

#3つまで選択できる、300個までの制約なので　300/3 = 100進数に見立てる
_ = II()

ans = []
for i in range(3):
    for j in range(1,100+1):
        ans.append(100**i * j)
print(len(ans))
print(*ans)

# W = II()
#
# done = [0] * (W+1)
# done[0] = 1
#
# i = 1
# ans = []
# while i <= W:
#     ans.append(i)
#     for k in range(W+1):
#         if i + k <= W:
#             if 0 < done[k] < 3 and i != k:
#                 if done[k+i]:
#                     done[k+i] = min(done[k+i],done[k] + 1)
#                 else:
#                     done[k+i] = done[k] + 1
#         else:
#             break
#
#     while i <= W and done[i]:
#         i += 1
#
# print(len(ans))
# print(*ans)