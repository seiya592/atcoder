#19:30:15~
N = int(input())
lst = [list(input().split()) for i in range(N)]


nList = []
for i in range(N):
   nList.append([i + 1,lst[i][0],int(lst[i][1])])
nList.sort(key=lambda x:x[2],reverse=True)
nList.sort(key=lambda x:x[1])

for l in nList:
    print(l[0])
