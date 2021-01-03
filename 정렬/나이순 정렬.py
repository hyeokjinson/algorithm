if __name__ == '__main__':
    n=int(input())

    arr=[]
    tmp=1
    for _ in range(n):
        a=list(map(str,input().split()))
        arr.append((int(a[0]),a[1],tmp))
        tmp+=1
    arr=sorted(arr,key=lambda x:(x[0],x[2]))

    for age,name,num in arr:
        print(age,name)