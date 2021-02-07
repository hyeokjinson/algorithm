if __name__ == '__main__':
    n=int(input())
    k=int(input())
    arr=list(map(int,input().split()))

    if k>=n:
        print(0)

    else:
        arr.sort()

        sub=[]

        for i in range(n-1):
            sub.append(arr[i+1]-arr[i])
        sub.sort()

        for i in range(k-1):
            sub.pop()
        print(sum(sub))