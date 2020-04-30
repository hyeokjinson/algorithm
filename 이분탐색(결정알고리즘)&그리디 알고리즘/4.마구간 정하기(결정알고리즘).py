def Count(len):
    cnt=1
    ep=res[0]
    for i in range(1,n):
       if res[i]-ep>=len:
            ep=res[i]
            cnt+=1
    return cnt

n,c=map(int,input().split())
res=[]
largest=0

for i in range(n):
    tmp=int(input())
    res.append(tmp)
    largest=max(tmp,largest)

res.sort()
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        result=mid
        lt=mid+1
    else:
        rt=mid-1
print(result)