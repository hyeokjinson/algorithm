n=int(input())
arr=list(map(int,input().split()))
sum=0
cnt=0
for i in arr:
    if i==1:
        sum+=i+cnt
        cnt+=1
    elif i==0:
        cnt=0
print(sum)