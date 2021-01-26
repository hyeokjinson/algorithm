from collections import deque,defaultdict
import sys


dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    q=deque()
    q.append(tmp)
    dist[tmp]=0

    while q:
        x=q.popleft()
        if x==123456789:
            return dist[x]

        s=str(x)
        k=s.find('9')
        x,y=k//3,k%3

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<3 and 0<=ny<3:
                nk=nx*3+ny
                ns=list(s)
                ns[k],ns[nk]=ns[nk],ns[k]
                nd=int(''.join(ns))

                if not dist.get(nd):
                    dist[nd]=dist[x]+1
                    q.append(nd)

    return -1
if __name__ == '__main__':
    dist=dict()

    tmp=''

    for i in range(3):
        a=input()
        a=a.replace(' ','')
        tmp+=a
    tmp=int(tmp.replace('0','9'))

    print(bfs())