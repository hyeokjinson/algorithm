n=int(input())
res=[]
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    res.append((a,b))

res.sort(reverse=True)
max=-217000000
for h,w in res:
    if w>max:
        cnt+=1
        max=w


print(cnt)