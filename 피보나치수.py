def pi(n):
    x,y=0,1
    for i in range(n):
        x,y=y,x+y
        return x

print(pi(int(input())))