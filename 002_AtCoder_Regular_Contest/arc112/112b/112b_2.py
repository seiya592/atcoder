def seisuuya_range(B, C):
    rtn = []  # 0 = min / 1 = max
    if C % 2 == 1:
        # 奇数
        n = (C - 1) // 2
        rtn.append((B * -1) - n)  # odd_min
        rtn.append((B * -1) + n)  # odd_max
    elif C % 2 == 0:
        # 偶数
        n = C // 2
        if n == 0:
            #Cが制約上1の時のみここを通る　even_maxとminの大きさが逆転する為
            rtn.append(B)
            rtn.append(B)
        else:
            rtn.append(B - n)  # even_min
            rtn.append(B + n - 1)  # even_max
    return rtn


B, C = map(int, input().split())

lst1 = seisuuya_range(B, C)
lst2 = seisuuya_range(B, C - 1)

range1 = lst1[1] - lst1[0] + 1
range2 = lst2[1] - lst2[0] + 1

overlap = max(0, min(lst1[1], lst2[1]) - max(lst1[0], lst2[0]) + 1)

print(range1 + range2 - overlap)
