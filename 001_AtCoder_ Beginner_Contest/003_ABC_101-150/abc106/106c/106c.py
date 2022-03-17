#21:31:40~
S = input()
K = int(input())

for i in range(len(S)):
    if S[i] != '1':
        print(S[i])
        exit()
    else:
        if i + 1 == K:
            print(1)
            exit()
