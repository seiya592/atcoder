# a,b = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import collections

N = int(input())
a = list(map(int, input().split()))

rtn = collections.Counter(a)
print(len(rtn))
