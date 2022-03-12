# N,X = (map(int, input().split()))
# ab = [list(map(int, input().split())) for i in range(N)]
#
# tmpX = X
# lst = []
# for jmp in ab:
#     max_num = max(jmp)
#     min_num = min(jmp)
#     tmpX -= min_num
#
#     lst.append(max_num - min_num)
#
# if tmpX == 0:
#     print('Yes')
#     exit()
#
# if tmpX < 0:
#     print('No')
#     exit()
#
# if tmpX in lst:
#     print('Yes')

#解説デバッグ
n, x = map(int, input().split())
dp = 1
for _ in range(n):
  a, b = map(int, input().split())
  dp = (dp << a) | (dp << b)
print("Yes" if ((dp >> x) & 1) == 1 else "No")