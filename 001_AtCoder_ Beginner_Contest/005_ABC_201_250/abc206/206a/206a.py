# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import  math

N = int(input())
r = math.floor(N * 1.08)

print('Yay!' if r < 206 else 'so-so' if r == 206 else ':(')