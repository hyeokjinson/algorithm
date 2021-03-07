def garo(i):
    #경사로를 놓은 곳 확인 리스트
    c=[0for _ in range(n)]

    for j in range(n-1):
        #가로길 중에서 현재 가로길크기-다음 가로길이 1보다 크면 0으로 리턴
        if abs(arr[i][j]-arr[i][j+1])>1:
            return 0

        #다음 길이 큰 경우
        if arr[i][j]<arr[i][j+1]:
            temp=[0 for _ in range(n)]
            #l개의 크기 만큼 길이 같아야 함 따라서 j-k가 0보다 작으면 거짓
            for k in range(l):
                if j-k<0:
                    return 0
                #k만큼 이동하는 동안 크기가 같지 않거나 이미 경사로가 있으면 거짓
                if arr[i][j]!=arr[i][j-k] or c[j-k]!=0:
                    return 0
                temp[j-k]=1
            c=temp
        #현재 길이 다음 길보다 큰 경우 오른쪽으로 이동해야댐
        elif arr[i][j]>arr[i][j+1]:
            temp=[0 for _ in range(n)]

            for k in range(l):
                #다음 길이가 n-1의 범위 에 넘어가면 거짓
                if j+k+1>=n:
                    return 0
                #다음 길이와 그 다음 길이가 같지 않거나 경사로가 있으면 거짓
                if arr[i][j+1]!=arr[i][j+k+1] or c[j+k+1]!=0:
                    return 0

                temp[j+k+1]=1
            c=temp
    return 1

def sero(j):
    c=[0 for _ in range(n)]

    for i in range(n-1):
        if abs(arr[i][j]-arr[i+1][j])>1:
            return 0
        if arr[i][j]<arr[i+1][j]:
            temp=[0 for _ in range(n)]

            for k in range(l):
                if i-k<0:
                    return 0
                if arr[i][j]!=arr[i-k][j] or c[i-k]!=0:
                    return 0
                temp[i-k]=1
            c=temp
        elif arr[i][j]>arr[i+1][j]:
            temp=[0 for _ in range(n)]

            for k in range(l):
                if i+k+1>=n:
                    return 0
                if arr[i+1][j]!=arr[i+k+1][j] or c[i+k+1]!=0:
                    return 0
                temp[i+k+1]=1
            c=temp
    return 1
if __name__ == '__main__':
    n,l=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]

    ans=0

    for i in range(n):
        ans+=garo(i)
        ans+=sero(i)
    print(ans)