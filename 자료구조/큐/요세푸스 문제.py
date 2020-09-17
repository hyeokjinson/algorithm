from _collections import deque

if __name__=="__main__":
    n,k=map(int,input().split())
    a=list(range(1,n+1))
    q=deque(a)
    res=[]
    while q:
        for i in range(k-1):
            tmp=q.popleft()
            q.append(tmp)
        res.append(str(q.popleft()))
    print("<%s>"%(", ".join(res)))