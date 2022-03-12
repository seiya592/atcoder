A, B ,K = map(int, input().split())
lst = []
for i in range(1,min(A,B)+ 1):
    if A % i == 0 and B % i == 0:
        lst.append(i)

print(lst[K * (-1)])

#5:52
