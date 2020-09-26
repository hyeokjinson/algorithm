n=int(input())
a=list(map(int,input().split()))
sep=[0]*n

for i in range(n):
    for j in range(n):
        if a[i]==0 and sep[j]==0:
            sep[j]=i+1
            break
        elif sep[j]==0:
            a[i]-=1
for x in sep:
    print(x,end=' ')