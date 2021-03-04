def check1(num):
    visit=[False]*1000000

    temp=num

    while True:
        res=0
        while temp:
            res+=(temp%10)*(temp%10)
            temp=temp//10
        if res==1:
            return True
        if not visit[res]:
            visit[res]=True
        else:
            return False
        temp=res

if __name__ == '__main__':
    n=int(input())
    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False
    res=[]
    for i in range(n+1):
        if arr[i]:
            res.append(i)
            for j in range(i*2,n+1,i):
                if arr[j]:
                    arr[j]=False


    for i in res:
        if arr[i]:
            if check1(i):
                print(i)

