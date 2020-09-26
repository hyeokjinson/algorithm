n=int(input())
data=list(map(int,input().split()))
data.sort()
cnt=0
res=0
for i in data:
    cnt+=1
    if cnt>=i:
        res+=1
        cnt=0
print(res)
