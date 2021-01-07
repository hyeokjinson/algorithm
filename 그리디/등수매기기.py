if __name__ == '__main__':
    n=int(input())

    arr=[0]

    for _ in range(n):
        arr.append(int(input()))

    res=0
    arr.sort()
    for idx,value in enumerate(arr):
        res+=abs(value-idx)
    print(res)