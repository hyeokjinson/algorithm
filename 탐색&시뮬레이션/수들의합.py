n,m=map(int,input().split())
a=list(map(int,input().split()))
sum=0
cnt=0
for i in range(n):
    sum=a[i]
    if sum == m:
        cnt += 1
    for j in range(i+1,n):
        sum+=a[j]
        if sum==m:
            cnt+=1

print(cnt)