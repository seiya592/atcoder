def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

cnt = 0
for i in range(1,100000):
    _10000 = i // 10000
    _1000 = (i % 10000) // 1000
    _100 = (i % 1000) // 100
    _10 = (i % 100) // 10
    _1 = i % 10
    if i > 1000:
        pass
    if 1 <= _10 <= 9 and 1<= _1 <= 9 and 1<= _100 <= 9 and 1 <= _1000 <= 9 and 1<= _10000 <= 9:
        if abs(_1 - _10) <= 1 and abs(_10 - _100) <= 1 and abs(_100 - _1000) <= 1 and abs(_1000 - _10000) <= 1:
            cnt += 1

print(cnt)