n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
        s-=1
        e+=1
        if s==0:
            s+=1
            e-=1
print(res)