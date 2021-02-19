if __name__ == '__main__':
    n=int(input())

    max_=-2147000000

    arr=list(map(int,input().split()))

    arr.insert(0,0)

    arr_lst=[0 for _ in range(n+1)]

    for i in range(1,n+1):
        arr_lst[i]=max(arr[i]+arr_lst[i-1],arr[i])
        max_=max(max_,arr_lst[i])

    print(max_)
