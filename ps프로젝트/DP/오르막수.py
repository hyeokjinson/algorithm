if __name__ == '__main__':
    n=int(input())

    dy=[[0 for _ in range(10)]for _ in range(1001)]

    for i in range(10):
        dy[1][i]=1

    for i in range(2,1001):
        for j in range(10):
            for k in range(j+1):
                dy[i][j]+=dy[i-1][k]

    print(sum(dy[n])%10007)