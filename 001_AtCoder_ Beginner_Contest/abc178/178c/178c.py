# 19:36:50~
N = int(input())

print((pow(10, N) - (pow(9, N)) * 2 + pow(8, N)) % ((10 ** 9) + 7))