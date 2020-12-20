from _collections import deque
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

if __name__ == '__main__':
    n,m,k=map(int,input().split())
    arr=[[deque()for _ in range(n)]for _ in range(n)]
    q=deque()
    for _ in range(m):
        r,c,m,s,d=map(int,input().split())
        arr[r-1][c-1].append((m,s,d))
        q.append((r-1,c-1))

    for _ in range(k):
        temp=[]
        qlen=len(q)

        for _ in range(qlen):
            x,y=q.popleft()
            for _ in range(len(arr[x][y])):
                m,s,d=arr[x][y].popleft()
                nx = (s * dx[d] + x) % n
                ny = (s * dy[d] + y) % n
                q.append((nx,ny))
                temp.append((nx,ny,m,s,d))

        for x,y,m,s,d in temp:
            arr[x][y].append((m,s,d))

        for i in range(n):
            for j in range(n):
                if len(arr[i][j])>1:
                    nm,ns,odd,even,flag=0,0,0,0,0
                    for idx,(m,s,d) in enumerate(arr[i][j]):
                        nm+=m
                        ns+=s
                        if idx==0:
                            if d%2==0:
                                even=1
                            else:
                                odd=1
                        else:
                            if even==1 and d%2==1:
                                flag=1
                            if odd==1 and d%2==0:
                                flag=1

                    nm//=5
                    ns//=len(arr[i][j])
                    arr[i][j]=deque()

                    if nm!=0:
                        for idx in range(4):
                            if flag==0:
                                nd=2*idx
                            else:
                                nd=2*idx+1
                            arr[i][j].append((nm,ns,nd))
    res=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                for m,s,d in arr[i][j]:
                    res+=m
    print(res)