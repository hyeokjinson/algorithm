n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
res=[[0]*i for i in range(1,n+1)]
res[0][0]=arr[0][0]
for i in range(1,n):
    for j in range(len(res[i])):
        if j==0:
            res[i][j]=res[i-1][j]+arr[i][j]
        elif 0<j<i:
            res[i][j]=max(res[i-1][j-1],res[i-1][j])+arr[i][j]
        else:
            res[i][j]=res[i-1][j-1]+arr[i][j]
print(max(res[-1]))