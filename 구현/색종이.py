if __name__ == '__main__':
    n=int(input())

    arr=[[0]*100 for _ in range(100)]

    for _ in range(n):
        x,y=map(int,input().split())

        for i in range(x,x+10):
            for j in range(y,y+10):
                arr[i][j]=1

    ans=0

    for raw in arr:
        ans+=raw.count(1)
    print(ans)