#20:18~
N,M = (map(int, input().split()))
image = [list(input())for i in range(N)]
temp = [list(input())for i in range(M)]

tempRow = M
tempCol = len(temp[0])

for i in range(N - tempRow + 1):
    for j in range(N - tempCol + 1):
        flg = True
        for row in range(tempRow):
            for col in range(tempCol):
                if image[i + row][j + col] != temp[row][col]:
                    flg = False
                    break
            if flg == False:
                break
        if flg == True:
            print('Yes')
            exit()

print('No')