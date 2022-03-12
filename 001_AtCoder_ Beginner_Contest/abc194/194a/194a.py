# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
A,B = (map(int, input().split()))

if (A+B) >= 15 and B >= 8:
    print(1)
elif (A+B) >= 10 and B>= 3:
    print(2)
elif (A+B) >= 3:
    print(3)
else:
    print(4)