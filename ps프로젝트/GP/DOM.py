from collections import deque

if __name__ == '__main__':
    n,m,p=map(int,input().split())
    channel=[-1]*(m+1)
    watched=[False]*(m+1)

    for i in range(n):
        a,b=map(int,input().split())
        if channel[b]==-1:
            channel[b]=a

    q=deque()
    q.append(p)
    res=0
    arr=[]

    while q:
        tmp=q.popleft()

        if not watched[channel[tmp]] and channel[tmp]!=-1:
            q.append(channel[tmp])
            watched[channel[tmp]]=True
            res+=1
            arr.append(channel[tmp])
        elif channel[tmp]==-1:
            break
        elif watched[channel[tmp]]:
            res=-1
            break
    print(res)
