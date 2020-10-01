T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    dp=[]
    index=0
    for i in range(n):
        dp.append(arr[index:index+m])
        index+=m

    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i==0:
                left_up=0
            else:
                left_up=dp[i-1][j-1]
            #왼쪽에서 오는 경우
            left=dp[i][j-1]
            #왼쪽 아래에서 오는경우
            if i==n-1:
                left_down=0
            else:
                left_down=dp[i+1][j-1]
            dp[i][j]=max(left_down,left,left_up)+dp[i][j]
    res=0
    for i in range(n):
        res=max(res,dp[i][m-1])
    print(res)