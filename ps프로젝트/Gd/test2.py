if __name__ == '__main__':
    n=int(input())
    visit=[False]*(n+1)
    arr=list(map(int,input().split()))
    cnt=1
    now=0
    while True:
        now += arr[now]
        cnt += 1
        if visit[now]==True:
            break
        visit[now]=True

    print(cnt)
