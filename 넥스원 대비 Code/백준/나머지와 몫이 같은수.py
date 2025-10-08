if __name__ == '__main__':

    n=int(input())
    sum_=0
    for num in range(1,n):
        sum_+=(n*num)+num
    print(sum_)