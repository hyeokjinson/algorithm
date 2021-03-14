if __name__ == '__main__':
    n=int(input())
    dy=[0]*31

    dy[2]=3

    for i in range(4,n+1,2):
        dy[i]=dy[i-2]*3+2
        for j in range(2,i-2,2):
            dy[i]+=dy[j]*2
    print(dy[n])
