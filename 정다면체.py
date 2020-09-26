n,m=map(int,input().split())
cnt=[0 for _ in range(n+m+5) ]
result=[]
max=-1000000
for i in range(1,n+1):
    for j in range(1,m+1):
        tmp=i+j
        cnt[tmp]+=1
for k in range(len(cnt)):
    if max<cnt[k]:
        max=cnt[k]
print(cnt)
for i in range(len(cnt)):
    if cnt[i]==max:
        print(i,end=' ')