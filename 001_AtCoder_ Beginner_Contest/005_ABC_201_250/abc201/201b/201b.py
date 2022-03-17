# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
N = int(input())
ST = [list(input().split()) for i in range(N)]
ST2 = []
for i,j in ST:
    ST2.append([i,int(j)])
ST2 = sorted(ST2, reverse=True,key=lambda x:x[1])
print(ST2[1][0])
