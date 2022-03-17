# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import copy
S = input()
maru = []
hatena =[]
batu = []

for i in range(len(S)):
    if S[i] == 'o':
        maru.append(i)
    elif S[i] == 'x':
        batu.append(i)
    else:
        hatena.append(i)
rtn = 0
for i in range(10000):
    count = len(maru)
    tmpmaru = copy.deepcopy(maru)
    for j in range(4):
        mozi = '{:04}'.format(i)
        tmp = int(mozi[j])
        if tmp in batu:
            break
        elif tmp in tmpmaru:
            tmpmaru.remove(tmp)
            count -= 1
        if count == 0 and j == 3:
            rtn += 1
print(rtn)
# for i in range(0x3FF):
#     count = len(maru)
#     for j in range(10):
#         tmp = (i >> j) & 1
#         if tmp == 1:
#             if batu in j:
#                 break
#             elif maru in j:
#                 count -= 1



# print(maru)
# print(hatena)
# print(batu)
# print(tmp)