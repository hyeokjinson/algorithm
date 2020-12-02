n,k=map(int,input().split())
n*=2

t=0
nagudo=list(map(int,input().split()))
robot=[0]*n
while nagudo.count(0)<k:

    t+=1
    nagudo.insert(0,nagudo.pop())
    robot.insert(0,robot.pop())
    robot[n//2-1]=0

    for (r,i) in sorted([(robot[i],i)for i in range(n) if robot[i]>0]):
        if robot[i+1]==0 and nagudo[i+1]>0:
            robot[i]=0
            robot[i+1]=r

            nagudo[i+1]-=1

    robot[n//2-1]=0

    if nagudo[0]>0:
        nagudo[0]-=1
        robot[0]=t+1
print(t)