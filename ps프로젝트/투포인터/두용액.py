if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))

    lt=0
    rt=n-1
    ans=arr[lt]+arr[rt]
    arr.sort()
    al=lt
    ar=rt
    while lt<rt:
        tmp=arr[lt]+arr[rt]

        if abs(tmp)<abs(ans):
            ans=tmp
            al=lt
            ar=rt
            if tmp==0:
                break
        if tmp<0:
            lt+=1
        else:
            rt-=1

    print(arr[al],arr[ar])