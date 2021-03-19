if __name__ == '__main__':
    n,c=map(int,input().split())
    m=int(input())
    box=[list(map(int,input().split()))for _ in range(m)]

    box.sort(key=lambda x:x[1])

    check=[c]*(n+1)
    ans=0
    for i in range(m):
        temp=c
        for j in range(box[i][0],box[i][1]):
            temp=min(temp,check[j])
        temp=min(temp,box[i][2])

        for j in range(box[i][0],box[i][1]):
            check[j]-=temp
        ans+=temp
    print(ans)