if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]

    min_=2147000000

    max_=-2147000000

    for price in prices:
        min_=min(price,min_)
        max_=max(max_,price-min_)

    print(max_)