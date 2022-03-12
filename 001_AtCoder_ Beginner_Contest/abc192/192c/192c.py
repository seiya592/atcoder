N,K = (map(int, input().split()))

target_num = N
for i in range(K):
    target_num_asc = int(''.join(sorted(str(target_num))))
    target_num_desc = int(''.join(sorted(str(target_num), reverse = True)))
    target_num = target_num_desc - target_num_asc

print(target_num)