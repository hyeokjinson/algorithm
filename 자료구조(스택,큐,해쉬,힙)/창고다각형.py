if __name__ == '__main__':
    n=int(input())
    max_h=-1
    max_h_id=-1
    min_l=1001
    max_l=-1
    input_data=[]

    for i in range(n):
        l,h=map(int,input().split())
        input_data.append((l,h))

        if l<min_l:
            min_l=l
        if l>max_l:
            max_l=l
        if h>max_h:
            max_h_id=l
            max_h=h

    h_data=[0]*(max_l+1)
    for L,H in input_data:
        h_data[L]=H

    res=0
    temp=0
    for i in range(max_h_id+1):
        if h_data[i]>temp:
            temp=h_data[i]
        res=res+temp

    temp=0
    for i in range(max_l,max_h_id,-1):
        if h_data[i]>temp:
            temp=h_data[i]
        res+=temp

    print(res)