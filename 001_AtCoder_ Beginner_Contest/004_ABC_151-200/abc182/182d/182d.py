#19:24:00~
N = int(input())
A = list(map(int, input().split()))
TurnEnd = [A[0]]
TurnMax = [A[0]]
for a in A[1:]:
    TurnMax.append(max(TurnMax[-1], TurnEnd[-1] + a))
    TurnEnd.append(TurnEnd[-1] + a)

rtn = 0
now = 0
for i,j in zip(TurnMax,TurnEnd):
    rtn = max(rtn, now + i)
    now = now + j

print(rtn)


# sign = 'm' if A[0] < 0 else 'p'
# tmp = [A[0]]
# tmp2 = A[0]
# rtn = max(0,tmp2)
#
#
# for a in A[1:]:
#     if a > 0:
#         tmp[-1] += a
#         sign = 'p'
#     elif a < 0:
#         if sign == 'm':
#             tmp[-1] += a
#         else:
#             tmp.append(a)
#         sign = 'm'
#
#     for t in tmp:
#         tmp2 += t
#         rtn = max(tmp2,rtn)
#
# print(rtn)