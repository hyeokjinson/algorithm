if __name__ == '__main__':
    n=input()
    dp=[[0 for _ in range(2)]for _ in range(len(n)+1)]

    if int(n[0])==0:
        print(0)
    else:
        dp[0][0]=1
        dp[1][0]=1
        for i in range(2,len(n)+1):
            if int(n[i-1])>0:
                dp[i][0]=sum(dp[i-1])%1000000
            if 10<=int(n[i-2:i])<=26:
                dp[i][1]=sum(dp[i-2])%1000000

        print(sum(dp[-1])%1000000)