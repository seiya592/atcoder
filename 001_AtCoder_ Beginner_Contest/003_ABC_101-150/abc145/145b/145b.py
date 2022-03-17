#20:12:10~
N = int(input())
S = input()
if N % 2 == 1:
    print('No')
    exit()

for i in range(0,N//2):
    if S[i] != S[i + (N // 2)]:
        print('No')
        exit()

print('Yes')