#19:09:50~
N,X = (map(int, input().split()))
recipes = []
for _ in range(N):
    recipes.append(int(input()))

rtn = 0

for recipe in recipes:
    X -= recipe
    rtn += 1

rtn += X // min(recipes)

print(rtn)