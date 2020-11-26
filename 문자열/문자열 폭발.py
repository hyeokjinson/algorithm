if __name__ == '__main__':
    text=input()
    bomb=input()

    ans=[]

    for x in text:
        ans.append(x)

        if len(ans)>=len(bomb):
            same=True

            for j in range(-1,(-len(bomb)-1),-1):
                if ans[j]!=bomb[j]:
                    same=False
                    break
            if same==True:
                a=0

                while a<len(bomb):
                    ans.pop()
                    a+=1
    if len(ans)==0:
        print('FRULA')
    else:
        print(''.join(map(str,ans)))