# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

#21:42:25~
N = int(input())
friendList = list(map(int, input().split()))
friendList.sort(reverse=True)
center = len(friendList) // 2
if len(friendList) % 2 == 0:
    #偶数
    print(sum(friendList[1:center]) * 2 + friendList[0])
else:
    #奇数
    print(sum(friendList[1:center]) * 2 + friendList[0] + friendList[center])
