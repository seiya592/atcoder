N,X = map(int,input().split())
listA = list(map(int, input().split()))

listB = [x for x in listA if x != X]

print(*listB)