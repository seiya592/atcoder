def sosu(lst):
    limit = 200
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)


A,B,C,D = (map(int, input().split()))
lst = []
sosu(lst)
flg = True
for x in range(A, B + 1):
    flg2 = True
    for y in range(C, D + 1):
        if x + y in lst:
          flg2 = False
    if flg2:
        flg = False
        break


if flg:
    print('Aoki')
else:
    print('Takahashi')






