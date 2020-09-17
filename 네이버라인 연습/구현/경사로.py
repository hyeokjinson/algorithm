def check(a):
    s=a[0]
    idx=1
    tmp=1
    while idx<len(a):
        if s==a[idx]:
            idx+=1
            tmp+=1
            continue
        elif s==a[idx]-1:
            if tmp<L:
                return False
            else:
                s=a[idx]
                tmp=1
                idx+=1
        elif s==a[idx]+1:
            i=0
            for _ in range(L):
                if idx+i>=len(a):
                    return False
                else:
                    if a[idx]!=a[idx+i]:
                        return False
                i+=1
            if idx+L>=len(a):
                return True
            else:
                tmp=0
                idx+=L
                s=a[idx-1]
        else:
            return False
    return True

arr.isd
if __name__=="__main__":
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