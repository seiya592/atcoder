N, L = (map(int, input().split()))
x = list(map(int, input().split()))
t1,t2,t3 = (map(int, input().split()))

time = [10**100] * (L + 1)
time[0] = 0

xList = [False] * (L + 1)
for xx in x:
    xList[xx] = True

for i in range(1,L + 1):

    time[i] = min(time[i], time[i - 1] + (t1 * 1))
    #act2
    if i >= 2:
        time[i] = min(time[i], time[i - 2] + (t1 * 1) + (t2 * 1))

    #act3
    if i >= 4:
        time[i] = min(time[i], time[i - 4] + (t1 * 1) + (t2 * 3))


    if xList[i]:
        time[i] += t3


# ans = time[L]
# for i in [L-3,L-2,L-1]:
#     if i >= 0:
#         ans = min(ans, time[i] + t1*0.5 + t2 * (2*(L-i)-1)//2)
#
# print(ans)
#
# print(2 * 0.5)
# print(2 // 2)

ans = time[L]

#jump中にゴール
for i in range(1,4):
    if L - i >= 0:
        ans = min(ans, time[L-i] + (t1 // 2) + (t2 // 2) + (t2 * (i - 1)))

print(ans)


# ゴールL　- 1 までの時間をtimeに代入済み
# あとはゴールからact123を逆算

# # ★残り距離1　
# goal1 = 10**100
# goal2 = 10**100
# goal3 = 10**100
# goal4 = 10**100
# goal5 = 10**100
# goal6 = 10**100
#
# if L >= 1:
#     # そのままact1
#     goal1 = time[L - 1] + t1
#     # ジャンプするact2,3同じ
#     goal2 = time[L - 1] + ((t1 + t2) *0.5)
#
# # ★残り距離2
# if L >= 2:
#     #act2
#     goal3 = time[L - 2] + (t1 * 1) + (t2 * 1)
#     #act3
#     goal4 = time[L-2] + ((t1 * 0.5) + (t2 * 1.5))
#
# # ★残り距離3
# if L >= 3:
#     #act3
#     goal5 = time[L-3] + ((t1 * 0.5) + (t2 * 2.5))
#
# if L >= 4:
#     goal6 = time[L - 4] + ((t1 * 1) + (t2 * 3))
#
# print(min(goal1,goal2,goal3,goal4,goal5,goal6))

