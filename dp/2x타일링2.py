n=int(input())
dy=[0]*(n+1)

for i in range(1,n+1):
    if i==1:
        dy[i]=1
        continue
    if i==2:
        dy[i]=3
        continue
    dy[i]=(dy[i-1]+(dy[i-2]*2))%10007
print(dy[n])