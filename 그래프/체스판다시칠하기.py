start_w = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

start_b =[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
def check(x,y,c_map):
    w_cnt=0
    b_cnt=0
    for i in range(8):
        for j in range(8):
            if x[i][j]!=c_map[i][j]:
                w_cnt+=1
            if y[i][j]!=c_map[i][j]:
                b_cnt+=1
    return min(w_cnt,b_cnt)

min_=217000000

if __name__=='__main__':
    n,m=map(int,input().split())
    arr=[list(map(str,input()))for _ in range(n)]

    for i in range(n-7):
        for j in range(m-7):
            c_map=[]
            c_map.append(arr[i][j:j+8])
            c_map.append(arr[i+1][j:j + 8])
            c_map.append(arr[i + 2][j:j + 8])
            c_map.append(arr[i + 3][j:j + 8])
            c_map.append(arr[i + 4][j:j + 8])
            c_map.append(arr[i + 5][j:j + 8])
            c_map.append(arr[i + 6][j:j + 8])
            c_map.append(arr[i + 7][j:j + 8])

            res=check(start_w,start_b,c_map)
            if min_>res:
                min_=res
    print(min_)

