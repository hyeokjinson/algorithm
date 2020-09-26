n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
max_=-247000000
for i in range(n):
    sum1=0
    sum2=0
    for j in range(n):
        sum1+=arr[i][j]
        sum2+=arr[j][i]
        if sum1>max_:
            max_=sum1
        if sum2>max_:
            max_=sum2

sum1=sum2=0
for i in range(n):
    sum1+=arr[i][i]
    sum2+=arr[i][n-1-i]
    if sum1>max_:
        max_=sum1
    if sum2>max_:
        max_=sum2
print(max_)