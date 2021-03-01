if __name__ == '__main__':
    n,k=map(int,input().split())

    mod=1000000000

    table=[1]
    table+=[0]*n

    for _ in range(1,k+1):
        for i in range(1,n+1):
            table[i]=(table[i]+table[i-1])%mod
    print(table[n])