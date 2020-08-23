import math

x,y=map(int,input().split())
val=int(y*100/x)
lt=1
rt=x+y
res=0
while lt<=rt:
    mid=(lt+rt)//2
    tmp=int((y+mid)*100/(x+mid))
    if tmp>val:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
if res==0:
    print(-1)
else:
    print(res)
