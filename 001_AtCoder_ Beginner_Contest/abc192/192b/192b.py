S = input()

for i in range(len(S)):
    if i % 2 == 1:
        if S[i].isupper():
            None
        else:
            print('No')
            exit()
    else:
        if S[i].islower():
            None
        else:
            print('No')
            exit()
print('Yes')
