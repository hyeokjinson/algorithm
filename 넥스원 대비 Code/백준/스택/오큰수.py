if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))

    res=[-1]*n
    tmp=list()
    for i in range(len(arr)):

        while len(tmp)>0 and arr[tmp[-1]]<arr[i]:
            res[tmp.pop()]=arr[i]

        tmp.append(i)
    print(*res)
