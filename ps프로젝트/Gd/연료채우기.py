import heapq

if __name__ == '__main__':
    n=int(input())

    q=[]

    for _ in range(n):
        heapq.heappush(q,list(map(int,input().split())))

    target,fuel=map(int,input().split())

    move=[]
    cnt=0

    while fuel<target:
        while q and q[0][0]<=fuel:
            gs,f=heapq.heappop(q)
            heapq.heappush(move,[-1*f,gs])

        if not move:
            cnt=-1
            break
        f,gs=heapq.heappop(move)
        fuel+=-1*f
        cnt+=1
    print(cnt)