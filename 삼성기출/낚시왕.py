dx=[-1,1,0,0]
dy=[0,0,1,-1]

if __name__ == '__main__':
    r,c,m=map(int,input().split())
    arr=[[[0,0,0]for _ in range(c)]for _ in range(r)]
    res=0

    for _ in range(m):
        x,y,s,d,z=map(int,input().split())

        arr[x-1][y-1]=[s,d-1,z]

    for wang in range(c):
        c_arr=[[[0,0,0]for _ in range(c)]for _ in range(r)]
        for i in range(r):
            _,_,z=arr[i][wang]
            if z:
                res+=z
                arr[i][wang]=[0,0,0]
                break

        for i in range(r):
            for j in range(c):
                s,d,z=arr[i][j]
                if z:
                    if d<2:
                        ns,nd,ni=s%(2*(r-1)),d,i
                        for _ in range(ns):
                            if ni==0 and nd==0:
                                nd=1
                            if ni==r-1 and nd==1:
                                nd=0
                            ni+=dx[nd]
                        _,_,nz=c_arr[ni][j]
                        if z>nz:
                            c_arr[ni][j]=[s,nd,z]
                    else:
                        ns,nd,nj=s%(2*(c-1)),d,j
                        for _ in range(ns):
                            if nj==0 and nd==3:
                                nd=2
                            if nj==c-1 and nd==2:
                                nd=3
                            nj+=dy[nd]
                        _,_,nz=c_arr[i][nj]
                        if z>nz:
                            c_arr[i][nj]=[s,nd,z]
                    arr[i][j]=[0,0,0]
        arr=c_arr[:]
    print(res)

