def check(array):
    s=array[0]
    idx=1
    tmp=1

    while idx<len(array):
        if s==array[idx]:
            idx+=1
            tmp+=1
            continue

        elif s==array[idx]-1:
            if tmp<L:
                return False
            else:
                s=array[idx]
                tmp=1
                idx+=1
        elif s==array[idx]+1:
            i=0
            for _ in range(L):
                if idx+i>=len(array):
                    return False
                else:
                    if array[idx]!=array[idx+i]:
                        return False
                    i+=1

            if idx+L>=len(array):
                return True
            else:
                tmp=0
                idx+=L
                s=array[idx-1]
        else:
            return False
    return True




if __name__ == '__main__':
    N,L=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(N)]
    cnt=0

    for i in range(N):
        a_copy=[]
        b_copy=[]
        for j in range(N):
            a_copy.append(arr[i][j])
            b_copy.append(arr[j][i])
        if check(a_copy):
            cnt+=1
        if check(b_copy):
            cnt+=1
    print(cnt)