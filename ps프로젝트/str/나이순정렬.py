if __name__ == '__main__':
    n=int(input())
    arr=[]

    for i in range(n):
        age,name=map(str,input().split())
        arr.append((int(age),i,name))

    arr.sort(key=lambda x:(x[0],x[1]))

    for x,y,z in arr:
        print(x,z)

