def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


S = I()

l = len(S)

start = 0
for i in range(0,l):
    if S[i] == 'a':
        start += 1
    else:
        break

end = 0
for i in range(l-1, -1, -1):
    if S[i] == 'a':
        end += 1
    else:
        break

if start <= end:
    for i in range(start, (l-1) - end):
        if S[i] == S[((l-1) - end) - (i-start)]:
            if i > ((l - 1) - end) - i:
                break
        else:
            print('No')
            exit()
else:
    print('No')
    exit()

print('Yes')