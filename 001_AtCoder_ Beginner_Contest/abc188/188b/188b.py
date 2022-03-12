N = int(input())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listSum = 0
for i in range(N):
    listSum += listA[i] * listB[i]

print('No' if listSum == 0 else 'Yes')