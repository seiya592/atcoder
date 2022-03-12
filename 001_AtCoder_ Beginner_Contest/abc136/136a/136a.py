#10:11:58~
A,B,C = (map(int, input().split()))
print(max(C - (A - B),0))