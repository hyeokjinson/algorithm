from collections import defaultdict

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    dic=defaultdict(list)

    for word in strs:
        dic[''.join(sorted(word))].append(word)

    print(list(dic.values()))