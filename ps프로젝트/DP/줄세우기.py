if __name__ == '__main__':
    n=int(input())

    arr=[int(input()) for _ in range(n)]

    dp=[[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i]=1
        for j in range(i+1,n):
            for k in range(j):
                if arr[k]<arr[j]:
                    dp[i][j]=max(dp[i][j],dp[i][k]+1)

    lis=0

    for i in range(n):
        lis=max(lis,max(dp[i]))

    ans=n-lis
    print(ans)