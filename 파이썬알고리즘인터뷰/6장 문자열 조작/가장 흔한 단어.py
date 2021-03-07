import re
from collections import Counter
if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    words=[word for word in re.sub('[^\w]',' ',paragraph).lower().split()if word not in banned]

    count=Counter(words)
    print(count.most_common(1)[0][0])