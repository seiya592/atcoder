# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

A,B,W = (map(int, input().split()))
rtnmax = (W * 1000) // A
if (W * 1000) % B == 0:
    rtnmin = (W * 1000) // B
else:
    rtnmin = (W * 1000) // B + 1

if rtnmin > rtnmax:
    print('UNSATISFIABLE')
else:
    print('{0} {1}'.format(rtnmin,rtnmax))

# W = W * 1000
# rtn = []
#
# tmp = 0
# for i in range(W // A + 1):
#     for j in range(W // B + 1):
#         if (i * A) + (j * B) == W:
#             rtn.append(i+j)
#
# if len(rtn) == 0:
#     print('UNSATISFIABLE')
# else:
#     print('{0} {1}'.format(min(rtn),max(rtn)))

