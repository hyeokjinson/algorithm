dx=[0,1,0,-1]
dy=[1,0,-1,0]

if __name__=="__main__":
    n=int(input())
    color='wryogb'
    arr=[[[]for _ in range(3)]for _ in range(6)]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                arr[i][j][k]