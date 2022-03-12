# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
rtn = 100000000
for i in range(N):
    tmp = 100000000
    for j in range(N):
        if i == j:
            tmp = min(tmp,AB[i][0] + AB[j][1])
        else:
            tmp = min(tmp,AB[j][1])
    rtn = min(rtn,max(tmp,AB[i][0]))
print(rtn)

# Amin = 1000000
# Bmin = 1000000
# ABmin = 1000000
# ABsum = []
# for ab in AB:
#     ABsum.append(ab[0] + ab[1])
#
#
# for i in range(N):
#     Aflg = False
#     Bflg = False
#     if AB[i][0] < Amin:
#         Aflg = True
#     if AB[i][1] < Bmin:
#         Bflg = True
#     if Aflg == True and Bflg == True:
#         None
#     else:
#         Amin = min(AB[i][0], Amin)
#         Bmin = min(AB[i][1], Bmin)
#
# print(min(min(ABsum),max(Amin,Bmin)))