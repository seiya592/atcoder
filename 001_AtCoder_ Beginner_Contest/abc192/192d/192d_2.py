X = input()
M = int(input())
d = int(max(X))


def cond(n):
    temp, m = 0, 1
    for x in X[::-1]:
        temp += int(x) * m
        m *= n
        if temp > M: return True
    return False


def binary_search(MIN, MAX, cond):
    left, right = MIN, MAX  # search range
    while right - left > 1:
        mid = (left + right) // 2
        if cond(mid):
            right = mid
        else:
            left = mid
    return right


if len(X) == 1:
    print(1 if d <= M else 0)
else:
    b = binary_search(d, M + 1, cond)
    print(max(b - 1 - d, 0))