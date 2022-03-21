def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


s = I()

print(int(s[0]+s[1]+s[2])+int(s[1]+s[2]+s[0])+int(s[2]+s[0]+s[1]))