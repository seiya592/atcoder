A,B = map(int,input().split())

a1 = A % 10
a10 = (A % 100) // 10
a100 = (A % 1000) // 100

b1 = B % 10
b10 = B % 100 // 10
b100 = B % 1000 // 100

a = a1 + a10 + a100
b = b1 + b10 + b100

if a < b:
    print(b)
else:
    print(a)

#6:34
