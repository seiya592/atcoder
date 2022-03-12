#22:27~
A,B,X = (map(int, input().split()))

def nibunki(min,max,X):
    while True:
        center = (min + max) // 2
        if (A * center) + (B * len(str(center))) <= X < (A * (center + 1)) + (B * len(str(center + 1))):
            print(center)
            exit()
        elif (A * center) + (B * len(str(center))) < X :
            min = center
            # nibunki(center,max,X)
        elif (A * center) + (B * len(str(center))) > X:
            # nibunki(min,center, X)
            max = center

if A+B > X:
    print(0)
    exit()

for j in range(9):
    i = 10 ** j
    k = 10 ** (j + 1)
    if (A * i) + (B * len(str(i))) <= X <= (A * k) + (B * len(str(k))):
        keta = i
        break
else:
    print(10**9)
    exit()

nibunki(keta,keta * 10,X)



# a = (X // A)
# b = (B * len(str(X)))
# # maxseisu = max((X // A) - (B * len(str(X))),1)
# # maxseisu = max(max(a,b)-min(a,b),1)
# maxseisu = max(min(a,b),1)
# if (A * 10**9) + (B * len(str(10))) < X:
#     print(10**9)
#     exit()
# if A+B > X:
#     print(0)
#     exit()
# ret = 0
# for i in range(maxseisu,1,-A):
#     tmp = (A * i) + (B * len(str(i)))
#     if tmp <= X:
#         ret = i - 1
#         break
#
# for i in range(ret,ret + A + A,1):
#     tmp = (A * i) + (B * len(str(i)))
#     if tmp >= X:
#         ret2 = i - 1
#         break
# print(ret2)