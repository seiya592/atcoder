#22:07:45~
A,B,C = (map(int, input().split()))

print('win' if A + B + C <= 21 else 'bust')