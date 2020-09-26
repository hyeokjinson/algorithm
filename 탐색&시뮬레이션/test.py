n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
m=int(input())
def sum1(x,n):
    res=0
    s=0
    e=n-1
    for i in range(n):
        for j in range(s,e+1):
            res+=x[i][j]
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1
    return res
for i in range(m):
    s,t,q=map(int,input().split())
    for j in range(q):
        if t==0:
            a[s-1].append(a[s-1].pop(0))
        elif t==1:
            a[s-1].insert(0,a[s-1].pop())
print(sum1(a,n))
