N = int(input())
j = 0
count = 0
rtn = 0
for i in range(1, N + 1, 2):
    j = 1
    count = 0
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1

    if count == 8:
        rtn += 1

print(rtn)

#17:29
