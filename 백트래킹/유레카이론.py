def dfs(L,sum_):
    global flag

    if L==3:
        if sum_==k:
            flag=True
            return
    if L>=3:
        return 0
    else:
        for i in range(45):
            dfs(L+1,sum_+arr[i])


if __name__ == '__main__':
    T=int(input())
    arr=[]
    for x in range(1,46):
        tmp=x*(x+1)/2
        arr.append(tmp)

    for _ in range(T):
        k=int(input())
        flag=False
        dfs(0,0)

        if flag:
            print(1)
        else:
            print(0)