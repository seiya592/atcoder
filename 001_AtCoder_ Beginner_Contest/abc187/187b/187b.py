N = int(input())
ten = [list(map(int,input().split())) for i in range(N)]

count = 0
for i in range(N):
    x = ten[i][0]
    y = ten[i][1]
    for j in range(i+1 , N):
        xx = ten[j][0]
        yy = ten[j][1]

        henka = (y - yy)/ (x - xx)

        if - 1 <= henka <= 1:
            count += 1

print(count)

#19:19
