if __name__ == '__main__':
    n=int(input())

    arr=[]

    for _ in range(n):
        word=input()
        word_len=len(word)
        arr.append((word,word_len))

    arr=sorted(list(set(arr)),key=lambda x:(x[1],x[0]))
    for x in arr:
        print(x[0])