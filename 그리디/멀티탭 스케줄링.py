if __name__ == '__main__':
    n,k=map(int,input().split())

    arr=list(map(int,input().split()))

    multitab=[0]*n
    cnt=0

    for i in range(k):
        flag=False

        for j in range(n):
            if arr[i]==multitab[j] or multitab[j]==0:
                flag=True
                multitab[j]=arr[i]
                break
        if flag:
            continue
        else:
            a=0
            for j in range(n):
                try:
                    if a<arr[i+1:].index(multitab[j]):
                        a=arr[i+1:].index(multitab[j])
                        b=j
                except:
                    a=-1
                    b=j
                    break
            multitab[b]=arr[i]
            cnt+=1
    print(cnt)

