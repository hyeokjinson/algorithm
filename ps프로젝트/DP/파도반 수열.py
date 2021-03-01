if __name__ == '__main__':
    padovan=[0]*100
    padovan[0:5]=1,1,1,2,2,3
    t=int(input())
    for i in range(6,100):
        padovan[i]=padovan[i-1]+padovan[i-5]

    for _ in range(t):
        n=int(input())

        print(padovan[n-1])