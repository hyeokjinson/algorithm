def check(i,j):
    num_list=[1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if arr[i][k] in num_list:
            num_list.remove(arr[i][k])
        if arr[k][j] in num_list:
            num_list.remove(arr[k][j])

    i//=3
    j//=3

    for p in range(i*3,(i+1)*3):
        for q in range(j*3,(j+1)*3):
            if arr[p][q] in num_list:
                num_list.remove(arr[p][q])
    return num_list

def dfs(x):
    global flag
    if flag:
        return

    if x==len(ch):
        for row in arr:
            print(*row)
        flag=True
        return
    else:
        i,j=ch[x]
        ans_list=check(i,j)

        for tmp in ans_list:
            arr[i][j]=tmp
            dfs(x+1)
            arr[i][j]=0

if __name__ == '__main__':
    arr=[list(map(int,input().split()))for _ in range(9)]

    ch=[]
    flag=False
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                ch.append((i,j))

    dfs(0)