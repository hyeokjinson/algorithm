n,m=map(int,input().split())
weight=list(map(int,input().split()))
weight.sort()
cnt=0
for i in range(len(weight)-1):
    for j in range(i+1,len(weight)):
        if weight[i]!=weight[j]:
            cnt+=1
print(cnt)