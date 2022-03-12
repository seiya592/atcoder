B, C = map(int, input().split())
# lst = []
# for i in range(C + 1):
#     if i == 0:
#         lst.append(B)
#     elif i % 2 == 1:
#         lst.append((B * - 1) + ((i // 2) * - 1))
#         lst.append((B - (i // 2)) * - 1)
#     else: #i % 2 == 0:
#         lst.append(B - (i // 2))
#
# print(list(dict.fromkeys(lst)))
# print(len(list(dict.fromkeys(lst))))
flg = False
if B == 0:
    rtn = C
elif B > 0:
    if B * 2 < C + 1:
        rtn = B * 2 + C
    else:
        rtn = C * 2 - 1

else:
    if C % 2 == 1:
        C + 1
        flg = True

    if abs(B) * 4 > C:
        rtn = C / 2 * 3
    else:
        rtn = abs(B) * 2 + C - 1

    if flg == True:
        rtn -= 1

print(rtn)
