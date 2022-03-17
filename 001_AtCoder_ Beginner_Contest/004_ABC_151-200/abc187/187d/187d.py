N = int(input())
listAB = [list(map(int,input().split())) for i in range(N)]
aoki = 0
takahashi = []
for i in listAB:
    aoki += i[0]
    takahashi.append(i[1] + (i[0]*2))

takahashi.sort(reverse=True)

hyou = 0
for i in range(len(takahashi)):
    hyou += takahashi[i]
    if aoki < hyou:
        print(i + 1)
        exit()

#12:32
