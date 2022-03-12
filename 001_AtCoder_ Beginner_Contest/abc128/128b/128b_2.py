#19:30:15~
#リファクタ
N = int(input())

nList = []
for i in range(N):
    shop,score = input().split()
    nList.append([i + 1,shop,int(score)])

print(nList)
nList.sort(key=lambda x:(x[1],-x[2]))
print(nList)

for l in nList:
    print(l[0])
