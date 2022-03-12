#19:34:25~
a,b,c,d = (map(int, input().split()))

num = []
num.append(a*c)
num.append(a*d)
num.append(b*c)
num.append(b*d)
print(max(num))