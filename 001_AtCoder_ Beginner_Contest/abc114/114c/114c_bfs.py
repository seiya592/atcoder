def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
from collections import deque
N = II()
Q = deque()

Q.append(0)
ans = 0
while len(Q):
    n = Q.popleft()

    for i in [n * 10 + 3,n * 10 + 5,n * 10 + 7]:
        if i > N:
            continue
        i_st = str(i)
        if i_st.find('3') >= 0 and i_st.find('5') >= 0 and i_st.find('7') >= 0:
            ans += 1
        Q.append(i)

print(ans)