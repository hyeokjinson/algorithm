if __name__ == '__main__':
    n=int(input())
    t=[]
    p=[]
    dp=[0]*(n+1)

    for _ in range(n):
        a,b=map(int,input().split())
        t.append(a)
        p.append(b)
    max_=0
    for i in range(n-1,-1,-1):
        time=t[i]+i

        if time<=n:
            dp[i]=max(p[i]+dp[time],max_)
            max_=dp[i]
        else:
            dp[i]=max_
    print(max_)