if __name__ == '__main__':
    n=int(input())

    arr=[]

    for i in range(n):
        arr.append((int(input()),i))

    after_arr=sorted(arr,key=lambda x:x[0])
    res=0
    for i in range(n):
        tmp=after_arr[i][1]-arr[i][1]
        res=max(res,tmp)
    print(res+1)