a,b = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
# N = int(input())

if (a + 1 == b) or (a == 1 and b == 10):
    print('Yes')
else:
    print('No')