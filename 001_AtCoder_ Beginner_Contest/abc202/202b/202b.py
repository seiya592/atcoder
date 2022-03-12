# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

def a(n):
    if n == '6':
        return '9'
    elif n == '9':
        return '6'
    else:
        return n

S = input()
S = S[::-1]
tmp = ''
for s in S:
    tmp += a(s)
print(tmp)