#21:30:45~
A,B,C,K = (map(int, input().split()))

if A < K :
    rtn = A
    K -= A
    if B < K:
        print(rtn - (K - B))
    else:
        print(rtn)
else:
    print(K)
