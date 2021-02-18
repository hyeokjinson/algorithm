if __name__ == '__main__':
    n,k=map(int,input().split())

    coin=[]

    for _ in range(n):
        coin.append(int(input()))

    dy=[10001]*(k+1)
    dy[0]=0

    for i in range(n):
        for j in range(coin[i],k+1):
            dy[j]=min(dy[j],dy[j-coin[i]]+1)
    print(dy[k]if dy[k]!=10001 else -1)