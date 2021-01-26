from collections import deque

def bfs():
    q.append(n)
    cnt=0

    while q:
        lenq=len(q)
        while lenq:
            x=q.popleft()

            if x==k:
                print(cnt)
                return
            if x*2<MAX and res[x*2]==0:
                q.append(x*2)
                res[x*2]=res[x]+1
            if x+1<MAX and res[x+1]==0:
                q.append(x+1)
                res[x+1]=res[x]+1
            if x-1>=0 and res[x-1]==0:
                q.append(x-1)
                res[x-1]=res[x]+1
            lenq-=1
        cnt+=1



if __name__ == '__main__':
    n,k=map(int,input().split())

    q=deque()
    MAX=100001
    res = [0 for _ in range(MAX)]
    bfs()