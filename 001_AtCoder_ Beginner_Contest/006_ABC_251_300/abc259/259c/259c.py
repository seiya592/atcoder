def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


S = I()
T = I()

s = []

tmp = ''
cnt = 0
snum = 0
for a in S:
    if tmp != a:
        s.append(a)
        tmp = a
        cnt = 0
    else:
        if cnt == 0:
            s.append(a)
            tmp = a
            cnt += 1
        else:
            snum += 1

t = []
tmp = ''
cnt = 0
tnum = 0
for a in T:
    if tmp != a:
        t.append(a)
        tmp = a
        cnt = 0
    else:
        if cnt == 0:
            t.append(a)
            tmp = a
            cnt += 1
        else:
            tnum += 1
s = ''.join(s)
t = ''.join(t)



def calc():
    sp = 0
    tp = 0
    scnt = 0
    tcnt = 0
    now = ''
    while len(S) > sp and len(T) > tp:
        if S[sp] == T[tp]:
            now = S[sp]
            sp += 1
            tp += 1
            continue
        else:
            if now == S[sp]:
                while now == S[sp]:
                    sp += 1
                    tcnt += 1
            else:
                while now == T[tp]:
                    tp += 1
                    scnt += 1
    scnt += len(T) - tp
    tcnt += len(S) - sp

    if len(S) + scnt <= 2*10**5 and len(S) + scnt <= 2*10**5:
        return True
    return False

if s == t and calc():
    print('Yes')
else:
    print('No')