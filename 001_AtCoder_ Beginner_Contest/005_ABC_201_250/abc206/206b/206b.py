N = int(input())
i = 1
rtn = 0
while True:
    rtn += i
    if rtn >= N:
        break
    i += 1

print(i)