if __name__ == '__main__':
    t=int(input())
    dp=[1,2,4]+[0]*7
    for _ in range(t):
        ans=0
        n=int(input())

        for i in range(3,n):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[n-1])