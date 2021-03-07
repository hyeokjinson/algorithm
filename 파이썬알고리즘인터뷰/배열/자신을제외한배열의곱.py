def solve():
    out=[]

    p=1

    for i in range(len(n)):
        out.append(p)
        p=p*n[i]

    p=1
    for i in range(len(n)-1,-1,-1):
        out[i]=p*out[i]
        p=p*n[i]

    return out
if __name__ == '__main__':
    n=[1,2,3,4]

    print(solve())