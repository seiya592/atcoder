#23:04:05~

N = int(input())
A = list(map(int, input().split()))

num = 2 ** N
tmp = min(max(A[:num // 2]),max(A[num // 2:]))
print(A.index(tmp) + 1)