def rotate(area):
    t,x,y,z,w=u,

if __name__ == '__main__':
    T=int(input())
    u=[['w']*3 for _ in range(3)]
    d=[['y']*3 for _ in range(3)]
    f=[['r']*3 for _ in range(3)]
    b=[['o']*3 for _ in range(3)]
    l=[['g']*3 for _ in range(3)]
    r=[['b']*3 for _ in range(3)]

    for _ in range(T):
        n=int(input())
        s=list(input().split())

        for area,dir in s:
            rotate(area,dir)
            rotate2()

            if dir=='-':
                rotate(area)
                rotate(area)