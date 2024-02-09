def multiply(*args):
    product = 1
    for num in args:
        product *= num

    print(product)

multiply(23, 45, 3)
multiply(23, 67, 578923)