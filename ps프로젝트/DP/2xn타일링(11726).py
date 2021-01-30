if __name__ == '__main__':
    dy=[0,1,2]
    n=int(input())
    for i in range(3,n+1):
        tmp=(dy[i-2]+dy[i-1])%10007
        dy.append(tmp)
    print(dy[n])
