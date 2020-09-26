t=int(input())
for _ in range(t):
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(2)]
    max_=-217000000
    dis=[[0]*n for _ in range(2)]
    dis[0][0]=arr[0][0]
    dis[1][0]=arr[1][0]
    dis[0][1]=dis[1][0]+arr[0][1]
    dis[1][1]=dis[0][0]+arr[1][1]
    for i in range(2,n):
        dis[0][i]=max(dis[1][i-1]+arr[0][i],dis[1][i-2]+arr[0][i])
        dis[1][i]=max(dis[0][i-1]+arr[1][i],dis[0][i-2]+arr[1][i])
    print(max(dis[0][n-1],dis[1][n-1]))
