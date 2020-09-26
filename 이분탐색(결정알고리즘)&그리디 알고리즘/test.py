k,n=map(int,input().split())
a=[]
def Count(len):
    cnt=0
    for x in a:
        cnt+=x//len
    return cnt
largest=0
for i in range(k):
    tmp=int(input())
    a.append(tmp)
    largest=max(tmp,largest)

lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)