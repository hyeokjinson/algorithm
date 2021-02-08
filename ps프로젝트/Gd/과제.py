if __name__ == '__main__':
    n=int(input())

    arr=[]
    day=0
    for _ in range(n):
        d,w=map(int,input().split())
        arr.append((d,w))
        day=max(d,day)


    arr=sorted(arr,key=lambda x:(x[1],x[0]),reverse=True)
    res=[0]*(day+1)
    for s,v in arr:
        if res[s]==0:
            res[s]=v
        else:
            for j in range(s-1,0,-1):
                if res[j]==0:
                    res[j]=v
                    break
    print(sum(res))