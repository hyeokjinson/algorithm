def find_block(x):
    max_block=[0,0]

    for j in range(x+1,W):
        if input_data[j]>=input_data[x]:
            return j
        if max_block[1]<=input_data[j]:
            max_block[1]=input_data[j]
            max_block[0]=j
    return max_block[0]

def fill_water(x,y):
    water=min(input_data[x],input_data[y])
    cnt=0
    for j in range(x+1,y):
        cnt+=water-input_data[j]
        input_data[j]=water
    return cnt

if __name__ == '__main__':
    H,W=map(int,input().split())
    input_data=list(map(int,input().split()))
    answer=0

    i=0
    while i<W-1:
        b=find_block(i)
        answer+=fill_water(i,b)
        i=b
    print(answer)


