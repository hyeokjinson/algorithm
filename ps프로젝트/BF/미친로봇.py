def solve(num,percent):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    stack=[]
    stack.append((0,0,num,1,[(0,0)]))

    ans=0

    while stack:
        x,y,count,per,path=stack.pop()
        if count==0:
            ans+=per
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx,ny) not in path:
                stack.append((nx,ny,count-1,per*percent[i],path+[(nx,ny)]))
    return ans

if __name__ == '__main__':
    n,east,west,south,north=map(int,input().split())
    percent=[east/100,west/100,south/100,north/100]

    if n==0:
        print(1)
    else:
        print(solve(n,percent))