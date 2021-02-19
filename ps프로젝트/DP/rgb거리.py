if __name__ == '__main__':
    n=int(input())

    house=[list(map(int,input().split())) for _ in range(n)]

    for i in range(1,n):
        house[i][0]=min(house[i-1][1],house[i-1][2])+house[i][0]
        house[i][1]=min(house[i-1][0],house[i-1][2])+house[i][1]
        house[i][2]=min(house[i-1][0],house[i-1][1])+house[i][2]
    print(min(house[n-1]))