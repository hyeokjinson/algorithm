n=int(input())
dy=[0]*(n+1)

for i in range(1,n+1):
    if i==1:
        dy[i]=1
        continue
    if i==2:
        dy[i]=2
        continue
    dy[i]=dy[i-2]+dy[i-1]
print(dy[n]%10007)