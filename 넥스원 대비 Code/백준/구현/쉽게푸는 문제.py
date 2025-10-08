if __name__ == '__main__':

    n,m=map(int,input().split())

    arr=[0]*1001
    cnt=0
    for i in range(1,1001):
        for j in range(i):
            if cnt > 1000:
                break
            arr[cnt]=i
            cnt+=1

    result=0
    for i in range(n-1,m):
        result+=arr[i]
    print(result)