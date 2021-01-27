import sys
if __name__ == '__main__':
    try:
        while True:
            s=input()
            up=0
            down=0
            num=0
            gong=0

            for x in s:
                if x.isalpha():
                    if x==x.upper():
                        up+=1
                    else:
                        down+=1
                elif x.isdigit():
                    num+=1
                elif x==' ':
                    gong+=1
            print(down,up,num,gong)
    except:
        sys.exit(0)
