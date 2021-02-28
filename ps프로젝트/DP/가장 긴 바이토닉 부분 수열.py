def left():
    dy=[0]*n

    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j] and dy[i]<dy[j]:
                dy[i]=dy[j]

        dy[i]+=1

    return dy

def right():
    dy=[0]*n

    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            if arr[i]>arr[j] and dy[i]<dy[j]:
                dy[i]=dy[j]
        dy[i]+=1
    return dy
if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    dy1=left()
    dy2=right()
    res=0
    for i in range(n):
        res=max(res,dy1[i]+dy2[i]-1)
    print(res)