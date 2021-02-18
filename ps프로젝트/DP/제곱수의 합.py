if __name__ == '__main__':
    n=int(input())
    dy=[0]*(n+1)

    for i in range(1,n+1):
        dy[i]=i

        for j in range(1,i):
            if (j*j)>i:
                break
            dy[i]=min(dy[i],dy[i-j*j]+1)
    print(dy[n])
