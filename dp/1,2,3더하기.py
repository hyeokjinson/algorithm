t=int(input())
dy=[]
dy.insert(0,0)
dy.insert(1,1)
dy.insert(2,2)
dy.insert(3,4)

for _ in range(t):
    n=int(input())
    for i in range(4,n+1):
        dy.insert(i,dy[i-1]+dy[i-2]+dy[i-3])
    print(dy[n])