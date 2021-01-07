if __name__ == '__main__':
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))

    res=0
    arr.sort()
    left=0
    right=n-1

    if n==1:
        print(arr[0])
    else:
        while left<right:
            if arr[left]<1 and arr[left+1]<1:
                res+=(arr[left]*arr[left+1])
                left+=2
            else:
                break
        while right>0:
            if arr[right]>1 and arr[right-1]>1:
                res+=(arr[right]*arr[right-1])
                right-=2
            else:
                break
        res+=sum([arr[i] for i in range(right,left-1,-1)])
        print(res)