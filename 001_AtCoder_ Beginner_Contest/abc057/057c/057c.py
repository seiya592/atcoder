# n = int(input())
#
# lower_divisors, upper_divisors = [], [1]
# i = 1
# while i * i <= n:       #←半分まで回す　low = A high = B で　A＜Bが成り立つ間　　　最大10**9だけど実質/2の計算量
#     if n % i == 0:      #1から探索して余りがない　＝　約数
#         lower_divisors.append(i)    #約数を小さい順に追加
#         if i != n // i:         #ルートで整数になる数のバカ避け
#             upper_divisors.append(n // i) #大きいほうの約数を追加
#     i += 1
#
#
# if lower_divisors[-1]**2 == n:
#     print(len(str(lower_divisors[-1])))
# elif upper_divisors[-1]**2 == n:
#     print(len(str(upper_divisors[-1])))
# else:
#     print(max(len(str(lower_divisors[-1])), len(str(upper_divisors[-1]))))
#
# #29m

n = int(input())

i = 1
while i * i <= n:  # ←半分まで回す　low = A high = B で　A＜Bが成り立つ間　　　最大10**9だけど実質/2の計算量
    if n % i == 0:
        result = max(len(str(i)), len(str(n // i)))  # n // i だとint型  n / i だとFloat型になる
    i += 1

# ループから抜けた時、直前の約数が中央の値
print(result)
