if __name__ == '__main__':
    n=int(input())
    arr=[]

    for i in range(n):
        arr.append(int(input()))

    arr.sort(reverse=True)
    max_=-2147000000

    for i in range(n):
        if arr[i]*(i+1)>=max_:
            max_=arr[i]*(i+1)
    print(max_)