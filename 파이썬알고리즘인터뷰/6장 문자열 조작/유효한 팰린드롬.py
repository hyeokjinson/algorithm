import sys

if __name__ == '__main__':
    s=input()
    solve=[]

    for x in s:
        if x.isalnum():
            solve.append(x.lower())

    while len(solve)>1:
        if solve.pop(0)!=solve.pop():
            print("false")
            sys.exit(0)
    print("true")

