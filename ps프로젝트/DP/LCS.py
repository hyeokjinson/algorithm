if __name__ == '__main__':
    s1=input()
    s2=input()
    dy=[[0]*(len(s2)+1)for _ in range(len(s1)+1)]

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dy[i][j]=dy[i-1][j-1]+1
            else:
                dy[i][j]=max(dy[i][j-1],dy[i-1][j])
    print(dy[len(s1)][len(s2)])