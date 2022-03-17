N = int(input())
a = list(map(int, input().split()))
i = 0
while i < N:

    if i >= len(a):
        break



    for j in range(1,a[i]):

        if a[i] != a[i+j]:
            break
    else:
        for k in range(1,a[i]):
            print(i+k)
        del a[i:i+a[i]]
        i -=1

    print(i + 1)
    i +=1

