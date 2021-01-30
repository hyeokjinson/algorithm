if __name__ == '__main__':
    dy=[0,1,2]

    n=int(input())

    for i in range(3,n+1):
        tmp=(dy[i-1]+dy[i-2])%15746
        dy.append(tmp)

    print(dy[n])
