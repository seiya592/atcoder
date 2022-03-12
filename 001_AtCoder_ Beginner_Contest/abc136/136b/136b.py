# N = int(input())
#
# if N == 100000:
#     rtn = 90909
# elif N >= 10000:
#     rtn = (((N // 10000)-1) * 10000)+(N % 10000) + 910
# elif N >= 1000:
#     rtn = 909
# elif N >= 100:
#     rtn = (((N // 100)-1) * 100)+(N % 100) + 10
# elif N >= 10:
#     rtn = 9
# else:
#     rtn = N % 10
#
# print(rtn)
# 17:00

#解説見た後
N = int(input())
rtn = 0
for i in range(1, N + 1):
    if len(str(i)) % 2 == 1:
        rtn += 1
print(rtn)
