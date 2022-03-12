# メモ化再帰練習
import sys

sys.setrecursionlimit(10000000) #再帰上限　必須！！！！

N = int(input())
h = list(map(int,input().split()))
init = 1000000000000
total = [init] * N
# total[0] = 0
done = [False] * N
# total[1] = total[0] + abs(h[0] - h[1])
# for i in range(2,N):
#     total[i] = min(total[i - 2] + abs(h[i-2] - h[i]), total[i -1] + abs(h[i-1]-h[i]))
#
# print(total[N-1])

# # debug
# class count:
#     __count = 0
#     @classmethod
#     def add(cls):
#         cls.__count += 1
#
#     @classmethod
#     def getC(cls):
#         return cls.__count


def dp(num):

    # count.add()
    if done[num]:
        return total[num]

    if num == 0:
        total[num] = 0
    elif num == 1:
        total[num] = dp(0) + abs(h[0] - h[1])
    else:
        total[num] = min(dp(num-1) + abs(h[num-1] - h[num]), dp(num-2) + abs(h[num-2] - h[num]))

    done[num] = True
    return total[num]

print(dp(N-1))
# print(count.getC())