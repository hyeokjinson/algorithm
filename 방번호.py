import math

num=list(map(int,input()))
set_num=[0]*9
for x in num:
    if x==9 or x==6:
        set_num[6]+=0.5
    else:
        set_num[x]+=1
print(int(max(set_num)))