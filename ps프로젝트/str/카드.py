if __name__ == '__main__':
    n=int(input())
    dic={}

    for _ in range(n):
        number=int(input())

        if number in dic:
            dic[number]+=1
        else:
            dic[number]=1

    dic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))

    print(dic[0][0])
