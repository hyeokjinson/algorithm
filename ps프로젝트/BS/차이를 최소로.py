from copy import deepcopy

def check(v):
    for i in range(n):
        c_arr[i]=arr[i]

    cnt=0

    for i in range(n-1):
        if c_arr[i+1]-c_arr[i]>v:
            cnt+=c_arr[i+1]-(c_arr[i]+v)
            c_arr[i+1]=c_arr[i]+v
    for i in range(n-1,0,-1):
        if c_arr[i-1]-c_arr[i]>v:
            cnt+=c_arr[i-1]-(c_arr[i]+v)
            c_arr[i-1]=c_arr[i]+v

    if cnt<=t:
        return True
    return False

if __name__ == '__main__':
    n,t=map(int,input().split())

    arr=list(map(int,input().split()))
    c_arr=[0]*n
    res=[0]*n
    lt=0
    rt=sum(arr)
    while lt<=rt:
        mid=(lt+rt)//2

        if check(mid):
            for i in range(n):
                res[i]=c_arr[i]
            rt=mid-1
        else:
            lt=mid+1
    for x in res:
        print(x,end=' ')