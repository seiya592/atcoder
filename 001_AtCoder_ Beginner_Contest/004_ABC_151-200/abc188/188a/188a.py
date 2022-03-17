X,Y = map(int,input('>>').split())

if X  > Y :
    if X < Y + 3:
        rtn = 'Yes'
    else:
        rtn = 'No'
else:
    if X + 3> Y:
        rtn = 'Yes'
    else:
        rtn = 'No'

print(rtn)