if __name__ == '__main__':
    n=int(input())
    dy=[0,0,1,1]

    for i in range(4,n+1):
        dy.append(dy[i-1]+1)

        if i%2==0:
            dy[i]=min(dy[i],dy[i//2]+1)
        if i%3==0:
            dy[i]=min(dy[i],dy[i//3]+1)
    print(dy[n])